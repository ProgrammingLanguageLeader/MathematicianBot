import logging

from telegram.error import TimedOut, TelegramError


def handle_errors(bot, update, error) -> None:
    logger = logging.getLogger(__name__)
    logger.warning('Update {} caused {} error'.format(update, error))
    try:
        raise error
    except TimedOut:
        pass
    except TelegramError:
        bot.send_message(
            chat_id=update.message.chat_id,
            text='Something went wrong... Please, post a new issue '
                 'on my GitHub repository to fix the problem'
        )
