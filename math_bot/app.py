from flask import Flask
from flask_migrate import Migrate

from math_bot.models import db
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db.app = app
db.init_app(app)
migrate = Migrate(app, db)
