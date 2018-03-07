from telegram import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, \
    ConversationHandler
import logging

from math_bot.app import db
from math_bot.tools import send_typing, write_logs, remember_new_user
from math_bot.wolfram import make_wolfram_query
from math_bot.models import User
from config import Config


START_MENU, MANUAL_QUERY, INTEGRAL, DERIVATIVE, LIMIT, SUM, \
    PLOT, EQUATION, TAYLOR_SERIES, EXTREMA, *_ = range(100)


@write_logs
@send_typing
@remember_new_user(simple_mode=True)
def handle_start(bot, update):
    chat_id = update.message.chat_id
    buttons = [
        KeyboardButton('Integral'),
        KeyboardButton('Derivative'),
        KeyboardButton('Limit'),
        KeyboardButton('Sum'),
        KeyboardButton('Plot'),
        KeyboardButton('Equation'),
        KeyboardButton('Extrema'),
        KeyboardButton('Taylor series'),
        KeyboardButton('Manual query'),
        KeyboardButton('Examples'),
        KeyboardButton('Help'),
        KeyboardButton('Cancel')
    ]
    keyboard = [buttons[i:i + 3] for i in range(0, len(buttons), 3)]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    bot.send_message(
        chat_id=chat_id,
        text='Choose one of the following options',
        reply_markup=reply_markup
    )
    return START_MENU


@write_logs
@send_typing
def handle_start_menu(bot, update):
    text = update.message.text.lower()
    handlers_dict = {
        'examples': handle_examples,
        'help': handle_help,
        'cancel': handle_cancel,
        'manual query': handle_manual_query,
        'integral': handle_integral,
        'derivative': handle_derivative,
        'limit': handle_limit,
        'sum': handle_sum,
        'plot': handle_plot,
        'equation': handle_equation,
        'extrema': handle_extrema,
        'taylor series': handle_taylor_series
    }
    if text in handlers_dict:
        handler = handlers_dict[text]
        return handler(bot, update)
    return handle_other_messages(bot, update)


@write_logs
@send_typing
def handle_manual_query(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter your query',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return MANUAL_QUERY


@write_logs
@send_typing
def handle_integral(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter a function to integrate. If you want to calculate '
             'definite integral, then type "from a to b" (example: '
             'x^3 from 1 to 2)',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return INTEGRAL


@write_logs
@send_typing
def handle_integral_query(bot, update):
    update.message.text = 'integrate {}'.format(update.message.text)
    return handle_wolfram_query(bot, update)


@write_logs
@send_typing
def handle_derivative(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter a function to calculate derivative',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return DERIVATIVE


@write_logs
@send_typing
def handle_derivative_query(bot, update):
    update.message.text = 'derivative {}'.format(update.message.text)
    return handle_wolfram_query(bot, update)


@write_logs
@send_typing
def handle_limit(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter a function/sequence to calculate limit with '
             'the number to which argument/number approaches '
             '(example: (1 + 1/x)^x x -> infinity)',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return LIMIT


@write_logs
@send_typing
def handle_limit_query(bot, update):
    update.message.text = 'limit {}'.format(update.message.text)
    return handle_wolfram_query(bot, update)


@write_logs
@send_typing
def handle_sum(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter a sequence to calculate sum. By default n = 0 '
             'to infinity, but you can setup other values '
             '(example: 1 / n^2, n = 1 to infinity)',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return SUM


@write_logs
@send_typing
def handle_sum_query(bot, update):
    update.message.text = 'sum {}'.format(update.message.text)
    return handle_wolfram_query(bot, update)


@write_logs
@send_typing
def handle_plot(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter a function to plot. You can set borders '
             '(example: 1/x from 10 to 100)',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return PLOT


@write_logs
@send_typing
def handle_plot_query(bot, update):
    update.message.text = 'plot {}'.format(update.message.text)
    return handle_wolfram_query(bot, update)


@write_logs
@send_typing
def handle_equation(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter an equation to solve '
             '(example: x^3 - 4x^2 + 6x - 24 = 0)',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return EQUATION


@write_logs
@send_typing
def handle_equation_query(bot, update):
    return handle_wolfram_query(bot, update)


@write_logs
@send_typing
def handle_extrema(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter a function to find extrema',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return EXTREMA


@write_logs
@send_typing
def handle_extrema_query(bot, update):
    update.message.text = 'extrema {}'.format(update.message.text)
    return handle_wolfram_query(bot, update)


@write_logs
@send_typing
def handle_taylor_series(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter a function to get taylor series',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return TAYLOR_SERIES


@write_logs
@send_typing
def handle_taylor_series_query(bot, update):
    update.message.text = 'taylor series {}'.format(update.message.text)
    return handle_wolfram_query(bot, update)


@write_logs
@send_typing
@remember_new_user(simple_mode=True)
def handle_help(bot, update):
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
    return handle_start(bot, update)


@write_logs
@send_typing
@remember_new_user(simple_mode=True)
def handle_examples(bot, update):
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
    return handle_start(bot, update)


@write_logs
@send_typing
def handle_detailed_mode(bot, update):
    db.session.query(User).filter_by(
        telegram_id=update.message.from_user.id
    ).update(dict(simple_mode=False))
    db.session.commit()
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Switched to detailed mode'
    )


@write_logs
@send_typing
def handle_simple_mode(bot, update):
    db.session.query(User).filter_by(
        telegram_id=update.message.from_user.id
    ).update(dict(simple_mode=True))
    db.session.commit()
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Switched to simple mode'
    )


@write_logs
@send_typing
def handle_wolfram_query(bot, update):
    current_user = db.session.query(User).filter_by(
        telegram_id=update.message.from_user.id
    ).all()[0]
    chat_id = update.message.chat_id
    text = update.message.text
    answer = make_wolfram_query(text)
    if answer.error or not answer.success:
        bot.send_message(
            chat_id=chat_id,
            text='Unsuccessful. Check your request and try again'
        )
        return
    for pod in (answer.pods[:3] if current_user.simple_mode else answer.pods):
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
    return handle_start(bot, update)


@write_logs
@send_typing
def handle_cancel(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Conversation was canceled. To start a new one use /start',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


@write_logs
@send_typing
def handle_other_messages(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Hello! Do you want to start working with me? If you do '
             'enter /start',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


def handle_errors(bot, update, error):
    logging.warning('Update {} caused {} error'.format(update, error))


def init_updater():
    updater = Updater(
        Config.TELEGRAM_TOKEN,
        request_kwargs={
            'read_timeout': 15,
            'connect_timeout': 15
        }
    )
    dispatcher = updater.dispatcher
    conversation_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', handle_start),
            MessageHandler(Filters.all, handle_other_messages)
        ],
        states={
            START_MENU: [
                MessageHandler(Filters.text, handle_start_menu),
                MessageHandler(Filters.all, handle_other_messages)
            ],
            MANUAL_QUERY: [
                MessageHandler(Filters.text, handle_wolfram_query)
            ],
            INTEGRAL: [
                MessageHandler(Filters.text, handle_integral_query)
            ],
            DERIVATIVE: [
                MessageHandler(Filters.text, handle_derivative_query)
            ],
            LIMIT: [
                MessageHandler(Filters.text, handle_limit_query)
            ],
            SUM: [
                MessageHandler(Filters.text, handle_sum_query)
            ],
            PLOT: [
                MessageHandler(Filters.text, handle_plot_query)
            ],
            EQUATION: [
                MessageHandler(Filters.text, handle_equation_query)
            ],
            TAYLOR_SERIES: [
                MessageHandler(Filters.text, handle_taylor_series_query)
            ],
            EXTREMA: [
                MessageHandler(Filters.text, handle_extrema_query)
            ]
        },
        fallbacks=[
            CommandHandler('cancel', handle_cancel)
        ]
    )
    dispatcher.add_handler(
        CommandHandler('help', handle_help)
    )
    dispatcher.add_handler(
        CommandHandler('examples', handle_examples)
    )
    dispatcher.add_handler(
        CommandHandler('simple_mode', handle_simple_mode)
    )
    dispatcher.add_handler(
        CommandHandler('detailed_mode', handle_detailed_mode)
    )
    dispatcher.add_handler(conversation_handler)
    dispatcher.add_error_handler(handle_errors)
    return updater
