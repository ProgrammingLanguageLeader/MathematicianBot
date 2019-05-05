from telegram import ReplyKeyboardRemove

from telegram_bot.handlers.utils.decorators import write_logs, send_typing, \
    remember_new_user
from telegram_bot.handlers.utils.menu_entries import MenuEntry


@write_logs
@send_typing
@remember_new_user
def handle_limit(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter a function/sequence to calculate limit with '
             'the number to which argument/number approaches '
             '(example: (1 + 1/x)^x x -> infinity)',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return MenuEntry.LIMIT.value
