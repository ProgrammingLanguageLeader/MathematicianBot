from flask import request
from telegram import Update
import logging

from math_bot.app import app
from math_bot.logic import init_updater
from config import Config


updater = init_updater()
updater.bot.set_webhook(
    url='https://%s/%s' % (Config.URL, Config.TELEGRAM_TOKEN),
    certificate=open(Config.CERTIFICATE_PATH, 'rb')
)
logging.basicConfig(
    filename=Config.BOT_LOG_PATH,
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
