#!/usr/bin/env python
# coding=utf-8

import os

from getenv import env

# debug
DEBUG = env('DEBUG', False)

# project path
cur_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
SYS_PATH = env('SYS_PATH', cur_dir)

# mysql
MYSQL_HOST = env("MYSQL_HOST", "localhost")
MYSQL_PORT = env("MYSQL_PORT", 3306)
MYSQL_USER = env("MYSQL_USER", "root")
MYSQL_PWD = env("MYSQL_PWD", "root")
MYSQL_DB = env("MYSQL_DB", "bnb_raw")
MYSQL_CHARSET = env("MYSQL_CHARSET", "utf8")

# logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        "console": {"level": "INFO", "class": "logging.StreamHandler", "formatter": "standard"},
        'logfile': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '{}/crawler_error.log'.format(env('LOG_DIR', '/data/logs')),
            'maxBytes': 5 * 1024 * 1024,
            'backupCount': 2,
            'formatter': 'standard',
        }
    },
    'loggers': {
        'debug': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'primary': {
            'handlers': ['logfile'],
            'level': 'INFO',
            'propagate': False,
        }
    }
}
