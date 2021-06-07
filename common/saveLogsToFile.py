from settings import app
from logging import Formatter, INFO
from logging.handlers import RotatingFileHandler
from os import path, mkdir


def saveLogsToFile():
    if not path.exists('logs'):
        mkdir('logs')
    file_handler = RotatingFileHandler('logs/logs.txt', maxBytes=1048576, backupCount=10)  # 10 файлов по 1Мб максимум
    file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(INFO)
    app.logger.info('App start')