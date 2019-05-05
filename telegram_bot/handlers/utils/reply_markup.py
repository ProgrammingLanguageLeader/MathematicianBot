from telegram import ReplyKeyboardMarkup, KeyboardButton


def create_main_reply_markup() -> ReplyKeyboardMarkup:
    buttons = [
        KeyboardButton('Integral'),
        KeyboardButton('Derivative'),
        KeyboardButton('Limit'),
        KeyboardButton('Sum'),
        KeyboardButton('Plot'),
        KeyboardButton('Equation'),
        KeyboardButton('Extrema'),
        KeyboardButton('Taylor series'),
        KeyboardButton('Manual request'),
        KeyboardButton('Examples'),
        KeyboardButton('Help'),
        KeyboardButton('Toggle mode')
    ]
    keyboard = [buttons[i:i + 3] for i in range(0, len(buttons), 3)]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    return reply_markup
