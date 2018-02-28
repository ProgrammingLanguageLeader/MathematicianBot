import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    HOME_DIR = '/srv/math_bot'

    URL = os.environ.get('URL')

    TELEGRAM_TOKEN = os.environ.get('MATH_BOT_TOKEN')
    WOLFRAM_APP_ID = os.environ.get('WOLFRAM_APP_ID')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
