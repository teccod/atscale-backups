# About
This application makes backup of you IRIS Adaptive Analytic's cubes to GitHub repository.

# Installation
Install this package by ZPM applet in IRIS BI.
```
zpm "install atscale-backups"
```
# Setup
After installation complete you have to configure module. You need know Adaptive Analytics servername, credentials, GitHub token and repository 
```
d ##class(AtScaleBackups.utils).setConfig(
"GitHub_username",
"GitHub_PersonalAccessToken",
"GitHub_Repository_Name",
"Delay_in_seconds_between_backups",
"AtScale_host_name(for example: localhost:10500)",
"AtScale_org(example: default)",
"AtScale_login",
"AtScale_password",
[{"name" : "ProjectName", "id": "ProjectID(for example: 2d93c2be-5a95-4bec-6731-102eeb5c8d8d)"}]
)
```
AtScale_org you can take from the URL:
![image](https://user-images.githubusercontent.com/41373877/184341154-42677302-3ad3-4fe5-bb68-016f15ce6103.png)

Project ID is also available from the URL:
![image](https://user-images.githubusercontent.com/41373877/184341315-6b577863-0eae-4b85-bd43-2d9b11346b82.png)

Module store its config in the /src/AtScaleBackups/config.ini file.

# Launch
To start backup process you have to execute this command in IRIS
```
d ##class(AtScaleBackups.utils).start()
```

After that first backup will be created. 
The process will be repeated with "Delay_in_seconds_between_backups" delay.
