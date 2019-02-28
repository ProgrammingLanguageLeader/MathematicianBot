from flask import current_app, request

from telegram.update import Update

from telegram_bot.blueprint import TelegramBlueprint
from telegram_bot.bot import TelegramBot
from telegram_bot.dispatcher import DispatcherProxy


telegram_blueprint = TelegramBlueprint()


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
