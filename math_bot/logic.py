from telegram import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, \
    ConversationHandler

from math_bot.app import db
from math_bot.tools import send_typing, write_logs, remember_new_user
from math_bot.wolfram import make_wolfram_query
from math_bot.models import User
from math_bot.error import error_handler
from config import Config


START_MENU, MANUAL_QUERY, INTEGRAL, DERIVATIVE, LIMIT, SUM, \
    PLOT, SOLVE_EQUATION, TAYLOR_SERIES, EXTREMA, *_ = range(100)


@write_logs
@send_typing
@remember_new_user(simple_mode=True)
def start(bot, update):
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
def start_menu(bot, update):
    text = update.message.text
    handlers_dict = {
        'Examples': examples,
        'Help': help,
        'Cancel': cancel,
        'Manual query': handle_manual_query,
        'Integral': handle_integral,
        'Derivative': handle_derivative,
        'Limit': handle_limit,
        'Sum': handle_sum,
        'Plot': handle_plot,
        'Equation': handle_equation,
        'Extrema': handle_extrema,
        'Taylor series': handle_taylor_series
    }
    handler = handlers_dict[text]
    return handler(bot, update)


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
    pass


@write_logs
@send_typing
def handle_derivative(bot, update):
    pass


@write_logs
@send_typing
def handle_limit(bot, update):
    pass


@write_logs
@send_typing
def handle_sum(bot, update):
    pass


@write_logs
@send_typing
def handle_plot(bot, update):
    pass


@write_logs
@send_typing
def handle_equation(bot, update):
    pass


@write_logs
@send_typing
def handle_extrema(bot, update):
    pass


@write_logs
@send_typing
def handle_taylor_series(bot, update):
    pass


@write_logs
@send_typing
@remember_new_user(simple_mode=True)
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
    return start(bot, update)


@write_logs
@send_typing
@remember_new_user(simple_mode=True)
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
    return start(bot, update)


@write_logs
@send_typing
def detailed_mode(bot, update):
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
def simple_mode(bot, update):
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
def wolfram_query(bot, update):
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
    for pod in (answer.pods[:2] if current_user.simple_mode else answer.pods):
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
    return start(bot, update)


@write_logs
@send_typing
def cancel(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Conversation was canceled. To start a new one use /start'
    )
    return ConversationHandler.END


def init_updater():
    updater = Updater(Config.TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher
    conversation_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', start),
            CommandHandler('help', help),
            CommandHandler('examples', examples)
        ],
        states={
            START_MENU: [
                MessageHandler(Filters.text, start_menu)
            ],
            MANUAL_QUERY: [
                MessageHandler(Filters.text, wolfram_query)
            ],
            INTEGRAL: [

            ],
            DERIVATIVE: [

            ],
            LIMIT: [

            ],
            SUM: [

            ],
            PLOT: [

            ],
            SOLVE_EQUATION: [

            ],
            TAYLOR_SERIES: [

            ],
            EXTREMA: [

            ]
        },
        fallbacks=[
            CommandHandler('cancel', cancel)
        ]
    )
    dispatcher.add_handler(
        CommandHandler('simple_mode', simple_mode)
    )
    dispatcher.add_handler(
        CommandHandler('detailed_mode', detailed_mode)
    )
    dispatcher.add_handler(conversation_handler)
    dispatcher.add_error_handler(error_handler)
    return updater
