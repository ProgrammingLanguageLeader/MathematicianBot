from flask import current_app

from telegram_bot.bot import TelegramBot


def set_webhook():
    host_url = current_app.config.get('HOST_URL')
    host_port = current_app.config.get('HOST_PORT')
    telegram_token = current_app.config.get('TELEGRAM_TOKEN')
    bot = TelegramBot(telegram_token)
    bot.set_webhook(
        url='%s:%s/telegram/%s' % (
            host_url,
            host_port,
            telegram_token
        )
    )
