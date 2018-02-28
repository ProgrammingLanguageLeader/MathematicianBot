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

## Long polling
Run polling.py to use this method. Virtual environment must be activated.
```bash
source venv/bin/activate
python polling.py
```

## Webhook
Coming soon  