from flask import Blueprint
from flask_cors import CORS

api_blueprint = Blueprint('api_blueprint', __name__)
CORS(api_blueprint)


@api_blueprint.route('/')
def check():
    return 'API root'


@api_blueprint.route('/simple')
def make_simple_request():
    return 'simple'


@api_blueprint.route('/detailed')
def make_detailed_request():
    return 'detailed'
