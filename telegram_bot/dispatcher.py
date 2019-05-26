from queue import Queue
from threading import Thread

from telegram import Bot
from telegram.ext import Dispatcher

from telegram_bot.handlers.conversation import get_conversation_handler
from telegram_bot.handlers.errors import handle_errors


def create_dispatcher(bot: Bot) -> Dispatcher:
    update_queue = Queue()
    dispatcher = Dispatcher(bot, update_queue)
    init_dispatcher(dispatcher)
    start_dispatcher_thread(dispatcher)
    return dispatcher


def init_dispatcher(dispatcher: Dispatcher) -> None:
    conversation_handler = get_conversation_handler()
    dispatcher.add_handler(conversation_handler)
    dispatcher.add_error_handler(handle_errors)


def start_dispatcher_thread(dispatcher: Dispatcher) -> Thread:
    dispatcher_thread = Thread(
        target=dispatcher.start,
        name='dispatcher',
        daemon=True
    )
    dispatcher_thread.start()
    return dispatcher_thread
