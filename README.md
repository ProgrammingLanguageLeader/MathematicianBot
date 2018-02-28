# MathematicianBot

This bot can solve different tasks using computational knowledge engine [Wolfram Alpha](https://www.wolframalpha.com/)

# How to install

Setup the following environment variables:
1. MATH_BOT_TOKEN - telegram token of the bot. It can be obtained from [BotFather](https://t.me/botfather).
2. WOLFRAM_APP_ID - an ID of the Wolfram Alpha application. Visit [WolframAlpha API](https://products.wolframalpha.com/api/) and register your app to get it.
3. MATH_BOT_DATABASE_URL - path to the database. 
4. _*(if you will host the app using VDS)*_ CERTIFICATE_PATH - path to your SSL certificate
5. _*(if you will host the app using VDS)*_ URL - URL of the hosting server

Setup environment variables on Linux:
```bash
export <NAME>=<VALUE>
```  

Python 3 should be already installed. Create virtual environment and use pip to install dependencies. Example on Linux:
```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```
You can install dependencies without virtual environment, but it's not recommended.

## Webhook
This is a guide about installation of this bot on Linux server.

Python 3, Nginx should be already installed. Use the following commands to create new user for the application.
```bash
sudo python3 create_user.py
```

Copy files of the project in to the <HOME_DIR> directory.
```bash
sudo cp -a <src> <HOME_DIR> 
```

Then log in as user that was created at the previous step. Create virtual environment and use pip to install dependencies:
```bash
sudo su - <APP_NAME> -s /bin/bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
exit
``` 

It's recommended to use reverse proxy, so Nginx config must contain the following strings:
```text
server {
    listen 443 default ssl;
    server_name <URL>;
    
    keepalive_timeout 60;
    ssl_certificate <CERTIFICATE_PATH>;
    ssl_certificate_key <PRIVATE_KEY_PATH>;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers  "HIGH:!RC4:!aNULL:!MD5:!kEDH";
    add_header Strict-Transport-Security 'max-age=604800';
    
    access_log /var/log/nginx_access.log;
    error_log /var/log/nginx_error.log;
}
```
After that, configure Nginx and uWSGI using _**deploy.py**_ script:
```bash
sudo su
cd <HOME_DIR>
source venv/bin/activate 
python deploy.py
exit
```
# How to manage

## Long polling
Activate virtual environment and launch _**polling.py**_ script to start the application. Example on Linux:
```bash
source venv/bin/activate
python polling.py
```
Press Ctrl + C to stop the bot. 

## Webhook
Service of the bot will be created after installation. To stop it just type in the terminal:
```bash
sudo systemctl stop <APP_NAME>
``` 
Another options is provided by [systemctl](https://www.unix.com/man-page/centos/1/systemctl/) program
