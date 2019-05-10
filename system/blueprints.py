def register_blueprints(app):
    with app.app_context():
        from telegram_bot.blueprint import telegram_blueprint
        from api.blueprint import api_blueprint

        app.register_blueprint(telegram_blueprint, url_prefix='/telegram')
        app.register_blueprint(api_blueprint, url_prefix='/api')
