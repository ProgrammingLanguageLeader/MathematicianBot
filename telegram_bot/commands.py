from flask.cli import AppGroup, with_appcontext

import telegram_bot.polling
import telegram_bot.webhook


telegram_cli = AppGroup('telegram')


@telegram_cli.command('polling')
@with_appcontext
def start_polling():
    """
    Starts telegram bot in the long-polling mode
    """
    telegram_bot.polling.start_polling()


@telegram_cli.command('webhook')
@with_appcontext
def start_webhook():
    """
    Starts telegram bot in the webhook mode
    """
    telegram_bot.webhook.set_webhook()
