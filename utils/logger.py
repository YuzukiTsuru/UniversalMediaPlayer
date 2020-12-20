from logging.config import dictConfig
from file import *

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s',
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
            'filename': get_custom_log_file_name(),
            'encoding': 'utf-8'
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['default', 'custom']
    }
})
