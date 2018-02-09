import logging

from app.bot import init_updater


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    updater = init_updater()
    updater.start_polling()
    updater.idle()
