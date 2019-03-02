from flask import Blueprint, render_template


web_site_routes = Blueprint('web_site_routes', __name__)


@web_site_routes.route('/')
def index():
    return render_template('web_site_routes/index.html')
