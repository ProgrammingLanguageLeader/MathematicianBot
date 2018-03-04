from telegram.error import TelegramError, NetworkError
from time import sleep
import logging


def handle_errors(bot, update, error):
    try:
        raise error
    except NetworkError:
        logging.exception('Update %s caused %s error' % (update, error))
        sleep(1)
        bot.send_message(
            text='A network error occurred',
            chat_id=update.message.chat_id
        )
    except TelegramError:
        logging.exception('Update %s caused %s error' % (update, error))
