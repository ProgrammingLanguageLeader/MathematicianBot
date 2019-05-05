from telegram_bot.handlers.utils.menu_entries import MenuEntry
from telegram_bot.handlers.utils.reply_markup import create_main_reply_markup
from telegram_bot.handlers.utils.decorators import write_logs, send_typing, remember_new_user


@write_logs
@send_typing
@remember_new_user
def handle_help_cmd(bot, update) -> int:
    chat_id = update.message.chat_id
    reply_markup = create_main_reply_markup()
    bot.send_message(
        chat_id=chat_id,
        text='The bot uses Wolfram Alpha computational language, '
             'so queries are the same as on this site.  Moreover, '
             'you can solve lots of non-mathematical problems, '
             'e.g. "What is the meaning of life?". To look at '
             'the examples just type /examples. Almost I support 2 '
             'modes: simple and detailed. Commands /simple_mode and '
             '/detailed_mode enables you to switch between them. '
             'Simple mode is using by default',
        reply_markup=reply_markup
    )
    return MenuEntry.START_MENU.value
