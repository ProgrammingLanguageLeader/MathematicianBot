# MathematicianBot

This bot can solve different tasks using computational knowledge engine [Wolfram Alpha](https://www.wolframalpha.com/)

# How to install

## Environment variables
Setup the following environment variables or specify them in a file __*.env*__ in the project root:
1. TELEGRAM_TOKEN - telegram token of the bot. It can be obtained from [BotFather](https://t.me/botfather).
2. WOLFRAM_APP_ID - an ID of the Wolfram Alpha application. Visit [WolframAlpha API](https://products.wolframalpha.com/api/) and register your app to get it.
3. DATABASE_URL - path to the database. 
4. HOST_URL and HOST_PORT - URL and PORT of the hosting server. If you are using long polling method, you may do not specify this.

## Python interpreter
Python 3.6 or higher should be already installed. Create virtual environment and use pip to install dependencies. Example on Linux:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
You can install dependencies without virtual environment, but it's not recommended.

## Database migrations
Run the following commands to migrate database
```bash
flask db upgrade
```
If you use Heroku, it can be done by Heroku CLI
```bash
heroku run upgrade
```

## Telegram bot with long polling mode
Run the following command under activated virtual environment:
```bash
flask telegram polling
```

## Backend deployment using Heroku
You can host the bot using [Heroku](https://dashboard.heroku.com/). Sign up on this site, install heroku-cli on your PC and run following commands:
```bash
heroku login
heroku create <your app name>
git push heroku master
```

## Frontend deployment using Github Pages
Simply go to the frontend folder and run a deployment script
```bash
cd frontend
./deploy.sh
```
