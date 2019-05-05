from io import BytesIO

from telegram.ext import run_async

from system.config import WOLFRAM_APP_ID
from system.db import db
from telegram_bot.handlers.utils.decorators import write_logs, send_typing, \
    remember_new_user
from telegram_bot.handlers.utils.menu_entries import MenuEntry
from telegram_bot.handlers.utils.reply_markup import create_main_reply_markup
from telegram_bot.handlers.utils.wolfram_parser import parse_wolfram_answer
from telegram_bot.models import User
from wolfram.api import make_wolfram_request, make_simple_wolfram_request


@run_async
@write_logs
@send_typing
@remember_new_user
def handle_wolfram_request(bot, update, prefix: str = '') -> int:
    chat_id = update.message.chat_id
    request = f'{prefix} {update.message.text}'.strip()
    current_user = db.session.query(User).filter_by(
        telegram_id=update.message.from_user.id
    ).first()
    reply_markup = create_main_reply_markup()

    if current_user.simple_mode:
        answer = make_simple_wolfram_request(request, WOLFRAM_APP_ID)
        if not answer:
            bot.send_message(
                chat_id=chat_id,
                text='Unsuccessful. Check your request and try again',
                reply_markup=reply_markup
            )
        else:
            bytes_io = BytesIO(answer)
            bot.send_photo(
                chat_id=chat_id,
                photo=bytes_io,
                reply_markup=reply_markup
            )
        return MenuEntry.START_MENU.value

    answer = make_wolfram_request(request, WOLFRAM_APP_ID)
    parsed_answer = parse_wolfram_answer(answer)
    for message in parsed_answer[:-1]:
        bot.send_message(
            chat_id=chat_id,
            text=message,
            parse_mode='Markdown'
        )
    bot.send_message(
        chat_id=chat_id,
        text=parsed_answer[-1],
        parse_mode='Markdown',
        reply_markup=reply_markup
    )
    return MenuEntry.START_MENU.value
