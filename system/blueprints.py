def register_blueprints(app):
    with app.app_context():
        from site.routes import site_routes
        from telegram_bot.routes import telegram_blueprint

        app.register_blueprint(site_routes)
        app.register_blueprint(telegram_blueprint, url_prefix='/telegram')
