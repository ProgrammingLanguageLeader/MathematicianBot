from flask import Blueprint, render_template


site_routes = Blueprint('site_routes', __name__)


@site_routes.route('/')
def index():
    return render_template('site/index.html')
