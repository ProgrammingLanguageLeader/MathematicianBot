from telegram_bot.handlers.utils.menu_entries import MenuEntry
from telegram_bot.handlers.utils.reply_markup import create_main_reply_markup
from telegram_bot.handlers.utils.decorators import write_logs, send_typing, remember_new_user


@write_logs
@send_typing
@remember_new_user
def handle_start_cmd(bot, update) -> int:
    chat_id = update.message.chat_id
    bot.send_message(
        chat_id=chat_id,
        text='Choose one of the following options or enter your request',
        reply_markup=create_main_reply_markup()
    )
    return MenuEntry.START_MENU.value
