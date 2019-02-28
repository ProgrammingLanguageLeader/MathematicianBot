from flask import Blueprint


system_blueprint = Blueprint('system_routes', __name__)


@system_blueprint.route('/')
def index():
    return 'It works'
