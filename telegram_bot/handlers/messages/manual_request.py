from telegram import ReplyKeyboardRemove

from telegram_bot.handlers.utils.decorators import remember_new_user, \
    send_typing, write_logs
from telegram_bot.handlers.utils.menu_entries import MenuEntry


@write_logs
@send_typing
@remember_new_user
def handle_manual_request(bot, update) -> int:
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter your request',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return MenuEntry.MANUAL_REQUEST.value
