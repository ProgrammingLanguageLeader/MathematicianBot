# MathematicianBot

This bot can solve different tasks using computational knowledge engine [Wolfram Alpha](https://www.wolframalpha.com/)

# How to install

At start you have to create config.py in the root directory of the project, which will have settings of the application:
```python
class Config:
    APP_NAME = '<application name>'
    CERTIFICATE_PATH = '<SSL certificate location>'
    TELEGRAM_TOKEN = '<telegram token>'
    URL = '<server URL>'
    WOLFRAM_APP_ID = '<application ID from WolframAlpha>'
    BOT_LOG_PATH = '<logging file location>'
```
Commentary:
1. _APP_NAME_ can be any string that you like;
2. _CERTIFICATE_PATH_ is a location of your SSL certificate. You can use self-signed certificate, get free one from [Let's Encrypt](https://letsencrypt.org/) or buy it;
3. _TELEGRAM_TOKEN_ is a token of your bot. Use [@BotFather](https://t.me/botfather) to get it;
4. _URL_ contains location of your bot and includes port number (if it's not default);
5. _WOLFRAM_APP_ID_ is an ID of your WolframAlpha app. Visit [WolframAlpha API](https://products.wolframalpha.com/api/) and register your app to get this ID;
6. _BOT_LOG_PATH_ is a location of logger. Notice, that this file should be able to write for the user which executes this bot.

Then Python 3 should be also already installed. Use pip to install dependencies:
```bash
pip install -r requirements.txt # alternatively try pip3
```
It's recommended to use [virtual environment](https://docs.python.org/3/tutorial/venv.html) for better isolation. 

After that, install and configure a web-server. It's recommended to use Nginx and uWSGI (the last has been already included to requirments.txt). Here is the [tutorial](https://www.digitalocean.com/community/tutorials/how-to-deploy-python-wsgi-applications-using-uwsgi-web-server-with-nginx).

Enjoy! (: