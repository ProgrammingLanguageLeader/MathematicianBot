import logging

from flask import current_app
from telegram import Bot


def set_webhook() -> Bot:
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    host_url = current_app.config.get('HOST_URL')
    host_port = current_app.config.get('HOST_PORT')
    telegram_token = current_app.config.get('TELEGRAM_TOKEN')
    bot = Bot(telegram_token)
    bot.set_webhook(
        url='%s:%s/telegram/%s' % (
            host_url,
            host_port,
            telegram_token
        )
    )
    return bot
