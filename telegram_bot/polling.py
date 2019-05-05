import logging
import time

from flask import current_app
from telegram import Bot

from telegram_bot.dispatcher import create_dispatcher


def start_polling():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG
    )
    bot = Bot(current_app.config['TELEGRAM_TOKEN'])
    bot.delete_webhook()
    dispatcher = create_dispatcher(bot)
    current_offset = 0
    while True:
        updates = bot.get_updates(offset=current_offset)
        for update in updates:
            dispatcher.update_queue.put(update)
            current_offset = update.update_id + 1
        time.sleep(1)
