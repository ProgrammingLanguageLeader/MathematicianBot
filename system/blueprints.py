def register_blueprints(app):
    with app.app_context():
        from web_site.routes import web_site_routes
        from telegram_bot.routes import telegram_blueprint

        app.register_blueprint(web_site_routes)
        app.register_blueprint(telegram_blueprint, url_prefix='/telegram')
