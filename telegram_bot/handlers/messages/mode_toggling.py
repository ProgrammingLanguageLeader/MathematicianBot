from system.db import db
from telegram_bot.handlers.utils.decorators import write_logs, send_typing, \
    remember_new_user
from telegram_bot.models import User


@write_logs
@send_typing
@remember_new_user
def handle_mode_toggling(bot, update) -> None:
    current_user = db.session.query(User).filter_by(
        telegram_id=update.message.from_user.id
    ).first()
    simple_mode = not current_user.simple_mode
    current_user.simple_mode = simple_mode
    db.session.commit()
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Switched to {} mode'.format(
            'simple' if simple_mode else 'detailed'
        )
    )
