from telegram import ReplyKeyboardRemove

from telegram_bot.handlers.utils.decorators import write_logs, send_typing, \
    remember_new_user
from telegram_bot.handlers.utils.menu_entries import MenuEntry


@write_logs
@send_typing
@remember_new_user
def handle_integral(bot, update) -> int:
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter a function to integrate. If you want to calculate '
             'definite integral, then type "from a to b" (example: '
             'x^3 from 1 to 2)',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return MenuEntry.INTEGRAL.value
