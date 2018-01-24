from flask import Flask, request
from telegram import Update

from config import Config
from app.logger import setup_logger
from app.webhook import setup_webhook


app = Flask(__name__)
logger = setup_logger()
logger.info('Application started')
dispatcher = setup_webhook()


@app.route('/%s' % Config.TELEGRAM_TOKEN, methods=['POST'])
def handle_webhook():
    update = Update.de_json(
        request.get_json(force=True),
        dispatcher.bot
    )
    dispatcher.process_update(update)
    return 'OK'
