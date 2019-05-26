from system.db import db
from telegram_bot.handlers.utils.decorators import write_logs, send_typing, \
    remember_new_user
from telegram_bot.handlers.utils.menu_entries import MenuEntry
from telegram_bot.handlers.utils.reply_markup import create_main_reply_markup
from telegram_bot.models import User


@write_logs
@send_typing
@remember_new_user
def handle_simple_mode_cmd(bot, update) -> int:
    db.session.query(User).filter_by(
        telegram_id=update.message.from_user.id
    ).update({
        'simple_mode': True
    })
    db.session.commit()
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Switched to simple mode',
        reply_markup=create_main_reply_markup()
    )
    return MenuEntry.START_MENU.value
