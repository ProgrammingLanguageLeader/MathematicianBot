from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, \
    ConversationHandler

from math_bot.app import db
from math_bot.tools import send_typing, write_logs, add_new_user
from math_bot.wolfram import make_wolfram_query
from math_bot.models import User
from math_bot.error import error_handler
from math_bot.conversation_states import ConversationStates
from config import Config


@write_logs
@send_typing
@add_new_user(ConversationStates.SIMPLE_MODE)
def start(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        chat_id=chat_id,
        text='Hello! I am mathematical bot. I was created '
             'to help people solve different tasks in '
             'mathematics. You can type /help to learn '
             'more about my functionality. To see examples '
             'use command /examples. Hope, you will like '
             'it. Good luck!'
    )
    current_user = db.session.query(User).filter_by(
        telegram_id=update.message.from_user.id
    ).all()[0]
    return current_user.mode


@write_logs
@send_typing
@add_new_user(ConversationStates.SIMPLE_MODE)
def help(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        chat_id=chat_id,
        text='The bot uses Wolfram Alpha computational language, '
             'so queries are the same as on this site.  Moreover, '
             'you can solve lots of non-mathematical problems, '
             'e.g. "What is the meaning of life?". To look at '
             'the examples just type /examples. Almost I support 2 '
             'modes: simple and detailed. Commands /simple_mode and '
             '/detailed_mode enables you to switch between them. '
             'Simple mode is using by default'
    )
    current_user = db.session.query(User).filter_by(
        telegram_id=update.message.from_user.id
    ).all()[0]
    return current_user.mode


@write_logs
@send_typing
@add_new_user(ConversationStates.SIMPLE_MODE)
def examples(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        chat_id=chat_id,
        text='Solve equation: solve x^2 + 2x + 1 = 0\n'
             'Maximize function: maximize x(1-x)e^x\n'
             'Minimize function: minimize x^2 + 2x + 1\n'
             'Compute an indefinite integral: integrate sin(x)\n'
             'Compute an definite integral: integrate sin(x) '
             'from 0 to pi\n'
             'Calculate a derivative: derivative of sin(x)\n'
             'Solve differential equation: y\'\' + y = 0\n'
             'Build a function graph: plot e^x\n'
             'To learn more examples visit '
             '[this site](http://www.wolframalpha.com/examples/math/)',
        parse_mode='Markdown',
        disable_web_page_preview=True
    )
    current_user = db.session.query(User).filter_by(
        telegram_id=update.message.from_user.id
    ).all()[0]
    return current_user.mode


@write_logs
@send_typing
@add_new_user(ConversationStates.DETAILED_MODE)
def detailed_mode(bot, update):
    db.session.query(User).filter_by(
        telegram_id=update.message.from_user.id
    ).update(dict(mode=ConversationStates.DETAILED_MODE))
    db.session.commit()
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Switched to detailed mode'
    )
    return ConversationStates.DETAILED_MODE


@write_logs
@send_typing
@add_new_user(ConversationStates.SIMPLE_MODE)
def simple_mode(bot, update):
    db.session.query(User).filter_by(
        telegram_id=update.message.from_user.id
    ).update(dict(mode=ConversationStates.SIMPLE_MODE))
    db.session.commit()
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Switched to simple mode'
    )
    return ConversationStates.SIMPLE_MODE


@write_logs
@send_typing
@add_new_user(ConversationStates.SIMPLE_MODE)
def detailed_wolfram_query(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    answer = make_wolfram_query(text)
    if answer.error or not answer.success:
        bot.send_message(
            chat_id=chat_id,
            text='Unsuccessful. Check your request and try again. Use /help '
                 'to see manual'
        )
        return
    for pod in answer.pods:
        title = pod.title
        bot.send_message(chat_id=chat_id, text=title)
        for sub in pod.subpods:
            text = sub.plaintext
            if text:
                bot.send_message(chat_id=chat_id, text=text)
            image_src = sub.img.src
            if image_src:
                bot.send_document(
                    chat_id=chat_id,
                    document=image_src,
                    timeout=15
                )
    return ConversationStates.DETAILED_MODE


@write_logs
@send_typing
@add_new_user(ConversationStates.SIMPLE_MODE)
def simple_wolfram_query(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    answer = make_wolfram_query(text)
    if answer.error or not answer.success:
        bot.send_message(
            chat_id=chat_id,
            text='Unsuccessful. Check your request and try again. Use /help '
                 'to see manual'
        )
        return
    for pod in answer.pods[:2]:
        title = pod.title
        bot.send_message(chat_id=chat_id, text=title)
        for sub in pod.subpods:
            text = sub.plaintext
            if text:
                bot.send_message(chat_id=chat_id, text=text)
            image_src = sub.img.src
            if image_src:
                bot.send_document(
                    chat_id=chat_id,
                    document=image_src,
                    timeout=15
                )
    return ConversationStates.SIMPLE_MODE


def init_updater():
    updater = Updater(Config.TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher
    conversation_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', start),
            CommandHandler('help', help),
            CommandHandler('examples', examples),
            MessageHandler(Filters.text, simple_wolfram_query)
        ],
        states={
            ConversationStates.SIMPLE_MODE: [
                CommandHandler('help', help),
                CommandHandler('examples', examples),
                CommandHandler('detailed_mode', detailed_mode),
                MessageHandler(Filters.text, simple_wolfram_query)
            ],
            ConversationStates.DETAILED_MODE: [
                CommandHandler('help', help),
                CommandHandler('examples', examples),
                CommandHandler('simple_mode', simple_mode),
                MessageHandler(Filters.text, detailed_wolfram_query)
            ]
        },
        fallbacks=[]
    )
    dispatcher.add_handler(conversation_handler)
    dispatcher.add_error_handler(error_handler)
    return updater


