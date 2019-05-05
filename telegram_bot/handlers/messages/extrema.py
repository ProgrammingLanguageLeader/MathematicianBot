from telegram import ReplyKeyboardRemove

from telegram_bot.handlers.utils.decorators import write_logs, send_typing, \
    remember_new_user
from telegram_bot.handlers.utils.menu_entries import MenuEntry


@write_logs
@send_typing
@remember_new_user
def handle_extrema(bot, update) -> int:
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter a function to find extrema',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return MenuEntry.EXTREMA.value