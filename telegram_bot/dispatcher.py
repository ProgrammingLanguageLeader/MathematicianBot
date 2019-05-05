from queue import Queue
from threading import Thread

from telegram import Bot
from telegram.ext import CommandHandler, MessageHandler, Filters, \
    ConversationHandler, Dispatcher

import telegram_bot.logic as logic
from telegram_bot.states import get_states


def create_dispatcher(bot: Bot) -> Dispatcher:
    update_queue = Queue()
    dispatcher = Dispatcher(bot, update_queue)
    init_dispatcher(dispatcher)
    start_dispatcher_thread(dispatcher)
    return dispatcher


def init_dispatcher(dispatcher):
    conversation_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', logic.handle_start),
            MessageHandler(Filters.all, logic.handle_start_menu)
        ],
        states=get_states(),
        fallbacks=[]
    )
    dispatcher.add_handler(
        CommandHandler('help', logic.handle_help)
    )
    dispatcher.add_handler(
        CommandHandler('examples', logic.handle_examples)
    )
    dispatcher.add_handler(
        CommandHandler('simple_mode', logic.handle_simple_mode)
    )
    dispatcher.add_handler(
        CommandHandler('detailed_mode', logic.handle_detailed_mode)
    )
    dispatcher.add_handler(conversation_handler)
    dispatcher.add_error_handler(logic.handle_errors)


def start_dispatcher_thread(dispatcher):
    dispatcher_thread = Thread(
        target=dispatcher.start,
        name='dispatcher',
        daemon=True
    )
    dispatcher_thread.start()
