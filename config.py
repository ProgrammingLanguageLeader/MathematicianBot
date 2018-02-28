import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    HOME_DIR = '/srv/math_bot'

    URL = os.environ.get('URL')
    NGINX_CONFIG_PATH = os.environ.get('NGINX_CONFIG_PATH')

    TELEGRAM_TOKEN = os.environ.get('MATH_BOT_TOKEN')
    WOLFRAM_APP_ID = os.environ.get('WOLFRAM_APP_ID')

    LOG_DIR = '/var/log/math_bot'
    UWSGI_LOG_PATH = '{}/uwsgi.log'.format(LOG_DIR)
    BOT_LOG_PATH = '{}/bot.log'.format(LOG_DIR)

    SQLALCHEMY_DATABASE_URI = os.environ.get('MATH_BOT_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
