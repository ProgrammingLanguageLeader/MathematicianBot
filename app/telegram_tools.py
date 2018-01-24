from telegram import ChatAction
from functools import wraps

from app.logger import get_logger


def pass_self(func):
    @wraps(func)
    def decorated(self, bot, update):
        return func(self, bot, update)
    return decorated


def send_typing(func):
    @wraps(func)
    def decorated(bot, update):
        chat_id = update.message.chat_id
        bot.send_chat_action(
            chat_id=chat_id,
            action=ChatAction.TYPING
        )
        return func(bot, update)
    return decorated


def write_logs(func):
    @wraps(func)
    def decorated(bot, update):
        logger = get_logger()
        user_id = update.message.from_user.id
        user_username = update.message.from_user.username
        action = update.message.text
        logger.info(
            'User %s:%s - %s' % (user_id, user_username, action)
        )
        return func(bot, update)
    return decorated
