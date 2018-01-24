from logging.handlers import RotatingFileHandler

import logging

from config import Config


def setup_logger():
    logger = logging.getLogger(Config.APP_NAME)
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler(
        filename=Config.BOT_LOG_PATH, maxBytes=100000, backupCount=1
    )
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_logger():
    return logging.getLogger(Config.APP_NAME)
