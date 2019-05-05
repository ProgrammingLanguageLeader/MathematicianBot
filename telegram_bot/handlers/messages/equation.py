from telegram import ReplyKeyboardRemove

from telegram_bot.handlers.utils.decorators import write_logs, send_typing, \
    remember_new_user
from telegram_bot.handlers.utils.menu_entries import MenuEntry


@write_logs
@send_typing
@remember_new_user
def handle_equation(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter an equation to solve '
             '(example: x^3 - 4x^2 + 6x - 24 = 0)',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return MenuEntry.EQUATION.value