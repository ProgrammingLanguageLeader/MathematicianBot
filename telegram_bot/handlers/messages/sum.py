from telegram import ReplyKeyboardRemove

from telegram_bot.handlers.utils.decorators import write_logs, send_typing, \
    remember_new_user
from telegram_bot.handlers.utils.menu_entries import MenuEntry


@write_logs
@send_typing
@remember_new_user
def handle_sum(bot, update) -> int:
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter a sequence to calculate sum. By default n = 0 '
             'to infinity, but you can setup other values '
             '(example: 1 / n^2, n = 1 to infinity)',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return MenuEntry.SUM.value
