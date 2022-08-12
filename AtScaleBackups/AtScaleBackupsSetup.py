import subprocess
import sys

def setup():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "configparser"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])