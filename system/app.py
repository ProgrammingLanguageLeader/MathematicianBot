import logging
import os
import sys

from flask import Flask

from system.blueprints import register_blueprints
from system.commands import register_commands
from system.db import db, migrate


def create_app():
    app = Flask(__name__, static_folder=None)
    app.url_map.strict_slashes = False
    app.config.from_object('system.config')
    if 'DYNO' in os.environ:
        app.logger.addHandler(logging.StreamHandler(sys.stdout))
        app.logger.setLevel(logging.INFO)

    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)
    register_blueprints(app)
    register_commands(app)
    return app
