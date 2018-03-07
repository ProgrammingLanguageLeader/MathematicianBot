# MathematicianBot

This bot can solve different tasks using computational knowledge engine [Wolfram Alpha](https://www.wolframalpha.com/)

# How to install

Setup the following environment variables:
1. MATH_BOT_TOKEN - telegram token of the bot. It can be obtained from [BotFather](https://t.me/botfather).
2. WOLFRAM_APP_ID - an ID of the Wolfram Alpha application. Visit [WolframAlpha API](https://products.wolframalpha.com/api/) and register your app to get it.
3. DATABASE_URL - path to the database. 
4. URL - URL of the hosting server. If you are using long polling method, you may do not specify this.

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

Run the following commands to migrate database
```bash
python manage.py db upgrade
python manage.py db migrate
```
If you use Heroku, it can be done by Heroku CLI
```bash
heroku run upgrade
heroku run migrate
```

## Long polling
Run *__polling.py__* to use this method. Virtual environment must be activated.
```bash
source venv/bin/activate
python polling.py
```

## Webhook
If you are using nginx, then you need to configure path to the SSL certificate and private key. For example
```text
server {
    listen              443 ssl;
    server_name         example.com;
    ssl_certificate     cert.pem;
    ssl_certificate_key private.key;

    location /BOT_TOKEN {
        proxy_pass http://127.0.0.1:5000;
    }
}
```
This example uses reverse proxy approach. It can be helpful, when you need to host several bots on the same server.

## Webhook on Heroku
Also you can host the bot on [Heroku](https://dashboard.heroku.com/). Sign up on this site, install heroku-cli on your PC and run following commands:
```bash
heroku login
heroku create <your app name>
git push heroku master
```
Enjoy (: