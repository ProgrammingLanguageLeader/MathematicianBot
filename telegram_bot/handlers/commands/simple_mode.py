from system.db import db
from telegram_bot.models import User
from telegram_bot.handlers.utils.decorators import write_logs, send_typing, remember_new_user


@write_logs
@send_typing
@remember_new_user
def handle_simple_mode_cmd(bot, update) -> None:
    db.session.query(User).filter_by(
        telegram_id=update.message.from_user.id
    ).update({
        'simple_mode': True
    })
    db.session.commit()
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Switched to simple mode'
    )
