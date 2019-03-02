from flask import current_app, request, Blueprint

from telegram.update import Update

from telegram_bot.bot import TelegramBot
from telegram_bot.dispatcher import DispatcherProxy


telegram_blueprint = Blueprint('telegram_blueprint', __name__)


@telegram_blueprint.route(
    '/%s' % current_app.config['TELEGRAM_TOKEN'],
    methods=['POST']
)
def webhook():
    bot = TelegramBot(current_app.config['TELEGRAM_TOKEN'])
    dispatcher = DispatcherProxy(bot)
    update = Update.de_json(request.get_json(force=True), bot=bot)
    dispatcher.update_queue.put(update)
    return 'OK'


@telegram_blueprint.route('/')
def check():
    return 'Telegram bot works'
