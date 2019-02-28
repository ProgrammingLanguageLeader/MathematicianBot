import click

from flask.cli import with_appcontext

import telegram_bot.polling
import telegram_bot.webhook


@click.command('polling')
@with_appcontext
def start_polling():
    telegram_bot.polling.start_polling()


@click.command('webhook')
@with_appcontext
def start_webhook():
    telegram_bot.webhook.set_webhook()


def register_commands(app):
    app.cli.add_command(start_polling)
    app.cli.add_command(start_webhook)
