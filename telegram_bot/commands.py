from flask.cli import AppGroup, with_appcontext

import telegram_bot.polling

telegram_cli = AppGroup('telegram')


@telegram_cli.command('polling')
@with_appcontext
def start_polling():
    """
    Starts telegram bot in the long-polling mode
    """
    telegram_bot.polling.start_polling()
