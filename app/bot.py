from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import Config
from app.error import error_handler
from app.logic import help, examples, start, wolfram_query


def init_updater():
    updater = Updater(Config.TELEGRAM_TOKEN)
    updater.bot.delete_webhook()
    dispatcher = updater.dispatcher
    add_handlers(dispatcher)
    return updater


def add_handlers(dispatcher):
    dispatcher.add_handler(
        CommandHandler('start', start)
    )
    dispatcher.add_handler(
        CommandHandler('help', help)
    )
    dispatcher.add_handler(
        CommandHandler('examples', examples)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.text, wolfram_query)
    )
    dispatcher.add_error_handler(error_handler)
    return dispatcher
