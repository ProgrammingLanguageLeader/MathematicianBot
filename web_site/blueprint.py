from flask import Blueprint, current_app, send_from_directory


DIST_DIR = current_app.config.get('DIST_DIR')
STATIC_DIR = current_app.config.get('STATIC_DIR')

web_site_blueprint = Blueprint(
    'web_site_blueprint',
    __name__,
    static_folder=STATIC_DIR,
    static_url_path='/static'
)


@web_site_blueprint.route('/')
def get_index_page():
    return send_from_directory(DIST_DIR, 'index.html')
