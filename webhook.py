import logging
import os

from math_bot.logic import init_updater
from config import Config


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    updater = init_updater()
    updater.start_webhook(
        listen='0.0.0.0',
        port=int(os.environ.get('PORT', '8443')),
        url_path=Config.TELEGRAM_TOKEN
    )
    updater.bot.set_webhook(
        url='{}/{}'.format(Config.URL, Config.TELEGRAM_TOKEN)
    )
    updater.idle()
