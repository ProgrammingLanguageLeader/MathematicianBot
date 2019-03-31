import os
import dotenv


BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
dotenv.load_dotenv(BASE_DIR)

DIST_DIR = os.path.join(BASE_DIR, 'web_site/frontend/dist')
STATIC_DIR = os.path.join(DIST_DIR, 'static')

HOST_URL = os.getenv('HOST_URL')
HOST_PORT = os.getenv('HOST_PORT') or 443

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
WOLFRAM_APP_ID = os.getenv('WOLFRAM_APP_ID')

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
    'sqlite:///%s' % os.path.join(BASE_DIR, 'db.sqlite3')
SQLALCHEMY_TRACK_MODIFICATIONS = False
