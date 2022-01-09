# Logging setup
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(message)s',
            # 'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
            'datefmt': '%d-%m-%Y %H:%M:%S',
        },
        'info_logger_format': {
            'format': '%(asctime)s %(message)s',
            'datefmt': '%d-%m-%Y %H:%M:%S'
        },
        'colored': {
            '()': 'colorlog.ColoredFormatter',
            # 'format': "%(asctime)s - %(name)s: %(log_color)s%(levelname)-4s%(reset)s %(blue)s%(message)s",
            'format': "%(asctime)s - %(log_color)s%(levelname)-4s%(reset)s %(blue)s%(message)s",
            'datefmt': '%d-%m-%Y %H:%M:%S'

        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/info.log',
            'maxBytes': 1024*1024*5,  # 5MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'debug_console_handler': {
            'level': 'DEBUG',
            'formatter': 'colored',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
        'repaying': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/repayments.log',
            'maxBytes': 1024 * 1024 * 5,  # 5MB
            'backupCount': 5,
            'formatter': 'info_logger_format'
        },
        'apscheduler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/apscheduler.log',
            'maxBytes': 1024 * 1024 * 5,  # 5MB
            'backupCount': 5,
        },
        'werkzeug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/werkzeug.log',
            'maxBytes': 1024 * 1024 * 5,  # 5MB
            'backupCount': 5,
        },
    },
    'loggers': {
        '': {
            'handlers': ['default', 'debug_console_handler'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'repaying': {
            'handlers': ['repaying'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'apscheduler': {
            'handlers': ['apscheduler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'werkzeug': {
            'handlers': ['werkzeug'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'urllib3.connectionpool': {
            'level': 'WARNING',
        }
    },
}