import logging
from functools import wraps

from telegram import ChatAction

from system.db import db
from telegram_bot.models import User


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
        logger = logging.getLogger(__name__)
        user_id = update.message.from_user.id
        user_username = update.message.from_user.username
        action = update.message.text
        logger.info(
            'User %s: %s - %s' % (user_id, user_username, action)
        )
        return func(bot, update)
    return decorated


def remember_new_user(func):
    @wraps(func)
    def decorated(bot, update):
        current_user = db.session.query(User).filter_by(
            telegram_id=update.message.from_user.id
        ).all()
        if not current_user:
            db.session.add(
                User(
                    telegram_id=update.message.from_user.id,
                    simple_mode=True
                )
            )
            db.session.commit()
        return func(bot, update)
    return decorated
