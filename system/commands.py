from telegram_bot.commands import telegram_cli


def register_commands(app):
    app.cli.add_command(telegram_cli)
