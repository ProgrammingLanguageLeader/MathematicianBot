def register_blueprints(app):
    with app.app_context():
        from web_site.blueprint import web_site_blueprint
        from telegram_bot.blueprint import telegram_blueprint
        from api.blueprint import api_blueprint

        app.register_blueprint(web_site_blueprint)
        app.register_blueprint(telegram_blueprint, url_prefix='/telegram')
        app.register_blueprint(api_blueprint, url_prefix='/api')
