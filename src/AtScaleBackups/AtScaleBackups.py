import base64
from datetime import date, datetime
import sched
import time
from traceback import print_tb
from requests import request
import requests
from configparser import ConfigParser
import json
import subprocess
import sys

config_path = "/opt/irisapp/src/AtScaleBackups/config.ini"
config = ConfigParser()
config.sections()
config.read(config_path)
s = sched.scheduler(time.time, time.sleep)

USERNAME = config['GitHub']['USERNAME']
TOKEN = config['GitHub']['TOKEN']
REPO = config['GitHub']['REPO']
DELAY = config['GitHub']['DELAY']
ATSCALE_HOST = config["AtScale"]['HOST']
ATSCALE_ORG = config['AtScale']['ORG']
ATSCALE_LOGIN = config['AtScale']['LOGIN']
ATSCALE_PASSWORD = config['AtScale']['PASSWORD']
PROJECTS = config['AtScale']['PROJECTS']


def get_bearer_token():
        token = base64.b64encode((f"{ATSCALE_LOGIN}:{ATSCALE_PASSWORD}").encode()).decode()
        return requests.get(f"http://{ATSCALE_HOST}/{ATSCALE_ORG}/auth", headers={'Authorization': f"Basic {token}"}).content.decode()

def get_file(project_id):
    return requests.get(f"http://{ATSCALE_HOST}/api/1.0/org/{ATSCALE_ORG}/project/{project_id}/xml",
    headers={'Authorization' : f"Bearer {get_bearer_token()}"}).json()['response']

def get_repos():
    return requests.get(
        f"https://api.github.com/search/repositories?q=user:{USERNAME}", 
        auth=("token", TOKEN)).json()

def create_file():
    s.enter(float(DELAY), 1, create_file)
    current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    for item in json.loads(config["AtScale"]["PROJECTS"]):
        path = f"/AtScale_backups/{current_time}/{item['name']}.xml"
        requests.put(f"https://api.github.com/repos/{USERNAME}/{REPO}/contents{path}", auth=("token", TOKEN), json={
            "owner" : "asda",
            "repo" : "test-atscale",
            "path" : path,
            "message" : f"Backup {current_time}",
            "content": base64.b64encode(str(get_file(item['id'])).encode()).decode()
        }).json()

def start():
    create_file()
    s.run()
    
def setup():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "configparser"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])

def setConfig(username, token, repo, delay, atscale_host, atscale_org, atscale_login, atscale_password, atscale_projects):
    config.set("GitHub", "USERNAME", username)
    config.set("GitHub", "TOKEN", token)
    config.set("GitHub", "REPO", repo)
    config.set("GitHub", "DELAY", delay)
    config.set("AtScale", "HOST", atscale_host)
    config.set("AtScale", "ORG", atscale_org)
    config.set("AtScale", "LOGIN", atscale_login)
    config.set("AtScale", "PASSWORD", atscale_password)
    config.set("AtScale", "PROJECTS", atscale_projects)

    with(open(config_path, "w")) as config_file:
        config.write(config_file)