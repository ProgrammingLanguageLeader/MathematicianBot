from system.routes import system_blueprint


def register_blueprints(app):
    with app.app_context():
        app.register_blueprint(system_blueprint)

        from telegram_bot.routes import telegram_blueprint
        app.register_blueprint(telegram_blueprint, url_prefix='/telegram')
