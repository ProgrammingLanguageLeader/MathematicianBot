import logging
from telegram import ChatAction
from functools import wraps

from math_bot.app import db
from math_bot.models import User


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
        user_id = update.message.from_user.id
        user_username = update.message.from_user.username
        action = update.message.text
        logging.info(
            'User %s:%s - %s' % (user_id, user_username, action)
        )
        return func(bot, update)
    return decorated


def add_new_user(mode):
    def arg_decorator(func):
        @wraps(func)
        def func_decorator(bot, update):
            current_user = db.session.query(User).filter_by(
                telegram_id=update.message.from_user.id
            ).all()
            if not current_user:
                db.session.add(
                    User(
                        telegram_id=update.message.from_user.id,
                        mode=mode
                    )
                )
                db.session.commit()
            return func(bot, update)
        return func_decorator
    return arg_decorator
