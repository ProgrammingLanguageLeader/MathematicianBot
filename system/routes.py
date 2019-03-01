from flask import Blueprint, render_template


system_blueprint = Blueprint('system_routes', __name__)


@system_blueprint.route('/')
def index():
    return render_template('system/index.html')
