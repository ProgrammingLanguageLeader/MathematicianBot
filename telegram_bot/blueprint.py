from flask import Blueprint

from utils.singleton import Singleton


@Singleton
class TelegramBlueprint(Blueprint):
    def __init__(self, *args):
        super().__init__('telegram_blueprint', __name__, *args)
