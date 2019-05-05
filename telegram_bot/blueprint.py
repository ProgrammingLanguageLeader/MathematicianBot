from flask import current_app, request, Blueprint
from telegram.ext import Dispatcher
from telegram.update import Update

from telegram_bot.dispatcher import create_dispatcher
from telegram_bot.webhook import set_webhook

telegram_blueprint = Blueprint('telegram_blueprint', __name__)


@telegram_blueprint.before_app_first_request
def init_telegram_blueprint():
    bot = set_webhook()
    create_dispatcher(bot)


@telegram_blueprint.route(
    '/%s' % current_app.config['TELEGRAM_TOKEN'],
    methods=['POST']
)
def webhook():
    dispatcher = Dispatcher.get_instance()
    update = Update.de_json(request.get_json(force=True), bot=dispatcher.bot)
    dispatcher.update_queue.put(update)
    return 'OK'


@telegram_blueprint.route('/')
def check():
    return 'Telegram bot works'
