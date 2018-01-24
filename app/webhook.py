from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import Config
from app.error import error_handler
from app.queries import handle_query
from app.commands import handle_start, handle_help, handle_examples


def setup_webhook():
    token = Config.TELEGRAM_TOKEN
    url = Config.URL
    certificate_path = Config.CERTIFICATE_PATH
    updater = Updater(token)
    updater.bot.delete_webhook()
    updater.bot.set_webhook(
        url='https://%s/%s' % (url, token),
        certificate=open(certificate_path, 'rb')
    )
    updater.dispatcher.add_handler(
        CommandHandler('start', handle_start)
    )
    updater.dispatcher.add_handler(
        CommandHandler('help', handle_help)
    )
    updater.dispatcher.add_handler(
        CommandHandler('examples', handle_examples)
    )
    updater.dispatcher.add_handler(
        MessageHandler(Filters.text, handle_query)
    )
    updater.dispatcher.add_error_handler(error_handler)
    return updater.dispatcher
