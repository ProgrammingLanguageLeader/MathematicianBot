from app.telegram_tools import send_typing, write_logs


@write_logs
@send_typing
def handle_start(bot, update):
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


@write_logs
@send_typing
def handle_help(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        chat_id=chat_id,
        text='The bot uses Wolfram Alpha computational language, '
             'so queries are the same as on this site.  Moreover, '
             'you can solve lots of non-mathematical problems, '
             'e.g. "What is the meaning of life?". To look at '
             'the examples just type /examples',
        parse_mode='Markdown'
    )


@write_logs
@send_typing
def handle_examples(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(
        chat_id=chat_id,
        text='Solve equation: solve x^2 + 2x + 1 = 0\n'
             'Maximize function: maximize x(1-x)e^x\n'
             'Minimize function: minimize x^2 + 2x + 1 = 0\n'
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
