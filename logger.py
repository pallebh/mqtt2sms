import logging
import logging.handlers
"""
logger
"""


def create_logger():
    """
    creates logger for screen and file
    """

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    logfilepath = "/var/log/mqtt2sms.log"
    log_file = logging.handlers.RotatingFileHandler(
        logfilepath, mode="a", maxBytes=1024 * 1024, backupCount=5)
    log_file.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s%(name)s:%(levelname)s:%(lineno)d:%(message)s',
        datefmt='%m/%d/%Y %H:%M:%S')
    log_file.setFormatter(formatter)
    logger.addHandler(log_file)

    log_console = logging.StreamHandler()
    log_console.setLevel(logging.DEBUG)
    log_console.setFormatter(formatter)
    logger.addHandler(log_console)

    return logger
