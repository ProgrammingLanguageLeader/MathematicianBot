from telegram import Bot

from utils.singleton import Singleton


@Singleton
class TelegramBot(Bot):
    pass
