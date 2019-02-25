from flask import Blueprint, current_app


routes_blueprint = Blueprint('system_routes', __name__)


@routes_blueprint.route('/')
def index():
    return 'It works'
