from flask import request
from telegram import Update
import logging
import os

from math_bot.app import app
from math_bot.logic import init_updater
from config import Config


updater = init_updater()
updater.start_webhook(
    listen='0.0.0.0',
    port=int(os.environ.get('PORT', '8443')),
    url_path=Config.TELEGRAM_TOKEN
)
updater.bot.set_webhook(
    url='{}/{}'.format(Config.URL, Config.TELEGRAM_TOKEN)
)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


@app.route('/{}'.format(Config.TELEGRAM_TOKEN), methods=['POST'])
def handle_update():
    dispatcher = updater.dispatcher
    update = Update.de_json(
        request.get_json(force=True),
        dispatcher.bot
    )
    dispatcher.process_update(update)
    return 'OK'
