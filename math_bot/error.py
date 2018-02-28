from telegram.error import TelegramError, NetworkError
from time import sleep
import logging


def error_handler(bot, update, error):
    try:
        raise error
    except NetworkError:
        sleep(1)
        bot.send_message(
            text='A network error occurred. Trying to answer again',
            chat_id=update.message.chat_id
        )
    except TelegramError:
        logging.exception("Update %s caused %s error" % (update, error))
