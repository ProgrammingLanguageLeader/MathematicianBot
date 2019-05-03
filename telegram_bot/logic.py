import logging

from telegram import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from system.config import WOLFRAM_APP_ID
from system.db import db

from telegram_bot.tools import send_typing, write_logs, remember_new_user
from telegram_bot.models import User
from telegram_bot.menu import MenuEntry
from telegram.error import TimedOut

from wolfram.requests import make_wolfram_request


@write_logs
@send_typing
@remember_new_user
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
        KeyboardButton('Toggle mode')
    ]
    keyboard = [buttons[i:i + 3] for i in range(0, len(buttons), 3)]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    bot.send_message(
        chat_id=chat_id,
        text='Choose one of the following options or enter your request',
        reply_markup=reply_markup
    )
    return MenuEntry.START_MENU.value


@write_logs
@send_typing
@remember_new_user
def handle_start_menu(bot, update):
    text = update.message.text.lower()
    handlers_dict = {
        'examples': handle_examples,
        'help': handle_help,
        'toggle mode': handle_mode_toggling,
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
@remember_new_user
def handle_manual_query(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter your query',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return MenuEntry.MANUAL_QUERY.value


@write_logs
@send_typing
@remember_new_user
def handle_integral(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter a function to integrate. If you want to calculate '
             'definite integral, then type "from a to b" (example: '
             'x^3 from 1 to 2)',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return MenuEntry.INTEGRAL.value


@write_logs
@send_typing
@remember_new_user
def handle_integral_query(bot, update):
    update.message.text = 'integrate {}'.format(update.message.text)
    return handle_wolfram_request(bot, update)


@write_logs
@send_typing
@remember_new_user
def handle_derivative(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter a function to calculate derivative',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return MenuEntry.DERIVATIVE.value


@write_logs
@send_typing
@remember_new_user
def handle_derivative_query(bot, update):
    update.message.text = 'derivative {}'.format(update.message.text)
    return handle_wolfram_request(bot, update)


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


@write_logs
@send_typing
@remember_new_user
def handle_limit_query(bot, update):
    update.message.text = 'limit {}'.format(update.message.text)
    return handle_wolfram_request(bot, update)


@write_logs
@send_typing
@remember_new_user
def handle_sum(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter a sequence to calculate sum. By default n = 0 '
             'to infinity, but you can setup other values '
             '(example: 1 / n^2, n = 1 to infinity)',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return MenuEntry.SUM.value


@write_logs
@send_typing
@remember_new_user
def handle_sum_query(bot, update):
    update.message.text = 'sum {}'.format(update.message.text)
    return handle_wolfram_request(bot, update)


@write_logs
@send_typing
@remember_new_user
def handle_plot(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter a function to plot. You can set borders '
             '(example: 1/x from 10 to 100)',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return MenuEntry.PLOT.value


@write_logs
@send_typing
@remember_new_user
def handle_plot_query(bot, update):
    update.message.text = 'plot {}'.format(update.message.text)
    return handle_wolfram_request(bot, update)


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


@write_logs
@send_typing
@remember_new_user
def handle_equation_query(bot, update):
    return handle_wolfram_request(bot, update)


@write_logs
@send_typing
@remember_new_user
def handle_extrema(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter a function to find extrema',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return MenuEntry.EXTREMA.value


@write_logs
@send_typing
@remember_new_user
def handle_extrema_query(bot, update):
    update.message.text = 'extrema {}'.format(update.message.text)
    return handle_wolfram_request(bot, update)


@write_logs
@send_typing
@remember_new_user
def handle_taylor_series(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        text='Enter a function to get taylor series',
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove()
    )
    return MenuEntry.TAYLOR_SERIES.value


@write_logs
@send_typing
@remember_new_user
def handle_taylor_series_query(bot, update):
    update.message.text = 'taylor series {}'.format(update.message.text)
    return handle_wolfram_request(bot, update)


@write_logs
@send_typing
@remember_new_user
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
@remember_new_user
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
@remember_new_user
def handle_detailed_mode(bot, update):
    db.session.query(User).filter_by(
        telegram_id=update.message.from_user.id
    ).update({
        'simple_mode': False
    })
    db.session.commit()
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Switched to detailed mode'
    )


@write_logs
@send_typing
@remember_new_user
def handle_simple_mode(bot, update):
    db.session.query(User).filter_by(
        telegram_id=update.message.from_user.id
    ).update({
        'simple_mode': True
    })
    db.session.commit()
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Switched to simple mode'
    )


@write_logs
@send_typing
@remember_new_user
def handle_wolfram_request(bot, update):
    current_user = db.session.query(User).filter_by(
        telegram_id=update.message.from_user.id
    ).first()
    chat_id = update.message.chat_id
    text = update.message.text
    answer = make_wolfram_request(text, WOLFRAM_APP_ID)
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
            image_src = '[Image]({})'.format(sub.img.src)
            if image_src:
                bot.send_message(
                    chat_id=chat_id,
                    text=image_src,
                    parse_mode='Markdown'
                )
    return handle_start(bot, update)


@write_logs
@send_typing
@remember_new_user
def handle_mode_toggling(bot, update):
    current_user = db.session.query(User).filter_by(
        telegram_id=update.message.from_user.id
    ).first()
    if current_user.simple_mode:
        return handle_detailed_mode(bot, update)
    return handle_simple_mode(bot, update)


@write_logs
@send_typing
@remember_new_user
def handle_other_messages(bot, update):
    return handle_wolfram_request(bot, update)


def handle_errors(bot, update, error):
    logging.warning('Update {} caused {} error'.format(update, error))
    try:
        raise error
    except TimedOut:
        pass
    except Exception:
        bot.send_message(
            chat_id=update.message.chat_id,
            text='Something went wrong... Please, post a new issue '
                 'on my GitHub repository to fix the problem'
        )
