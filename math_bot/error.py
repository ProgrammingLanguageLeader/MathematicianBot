from telegram.ext import Dispatcher
from telegram.error import TelegramError, NetworkError
from time import sleep

import logging

from config import Config


def error_handler(bot, update, error):
    logger = logging.getLogger(Config.APP_NAME)
    try:
        raise error
    except NetworkError:
        logger.exception('Update %s caused %s error' % (update, error))
        sleep(1)
        dispatcher = Dispatcher.get_instance()
        dispatcher.process_update(update)
    except TelegramError:
        logger.exception("Update %s caused %s error" % (update, error))
