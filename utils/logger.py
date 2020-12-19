import os
import time
from logging.config import dictConfig

from config import *


def get_custom_file_name():
    def make_dir(make_dir_path):
        path = make_dir_path.strip()
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    file_name = 'ump-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
    file_folder = os.path.abspath(os.path.dirname(__file__)) + os.sep + LOG_ROOT
    make_dir(file_folder)
    return file_folder + os.sep + file_name


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s',
    }},
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },
        'custom': {
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': get_custom_file_name(),
            'encoding': 'utf-8'
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['custom']
    }
})
