from flask import Flask

from system.routes import routes_blueprint


app = Flask(__name__)
app.config.from_object('system.config')
app.register_blueprint(routes_blueprint)
