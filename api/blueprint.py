from io import BytesIO

from flask import Blueprint, jsonify, request, current_app, send_file
from flask_cors import CORS
from werkzeug.exceptions import BadRequest

from wolfram.api import make_simple_wolfram_request

api_blueprint = Blueprint('api_blueprint', __name__)
CORS(api_blueprint)


@api_blueprint.route('/')
def check():
    return jsonify('API root')


@api_blueprint.route('/simple')
def make_simple_request():
    app_id = current_app.config.get('WOLFRAM_APP_ID')
    wolfram_request = request.args.get('request')
    if not wolfram_request:
        raise BadRequest('request must be set')
    response = make_simple_wolfram_request(
        wolfram_request,
        app_id,
        width=300,
        background='white',
        foreground='black'
    )
    response_bytes_io = BytesIO(response)
    return send_file(response_bytes_io, mimetype='image/gif')
