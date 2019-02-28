from flask import Flask

from system.db import db, migrate
from system.blueprints import register_blueprints
from system.commands import register_commands


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object('system.config')

    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)
    register_blueprints(app)
    register_commands(app)

    return app
