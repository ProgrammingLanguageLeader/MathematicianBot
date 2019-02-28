import logging
import time

from flask import current_app

from telegram_bot.dispatcher import DispatcherProxy
from telegram_bot.bot import TelegramBot


def start_polling():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    bot = TelegramBot(current_app.config['TELEGRAM_TOKEN'])
    dispatcher = DispatcherProxy(bot)
    current_offset = 0
    while True:
        updates = bot.get_updates(offset=current_offset)
        print(current_offset)
        for update in updates:
            print(updates)
            dispatcher.update_queue.put(update)
            current_offset = update.update_id + 1
        time.sleep(1)
