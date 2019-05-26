from telegram_bot.handlers.utils.decorators import write_logs, send_typing, \
    remember_new_user
from telegram_bot.handlers.utils.menu_entries import MenuEntry
from telegram_bot.handlers.utils.reply_markup import create_main_reply_markup


@write_logs
@send_typing
@remember_new_user
def handle_unknown_message(bot, update) -> int:
    chat_id = update.message.chat_id
    bot.send_message(
        text='I don\'t know what to say. '
             'Anyway catch the sticker 😉',
        chat_id=chat_id,
        reply_markup=create_main_reply_markup()
    )
    sticker_file_id = 'CAADAgADigIAAvilfQKsvnIfLjgE8QI'
    bot.send_sticker(chat_id, sticker_file_id)
    return MenuEntry.START_MENU.value
