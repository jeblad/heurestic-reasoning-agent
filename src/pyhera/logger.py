
#import time
import logging

logger = None
logHandle = None

def init(filename, dbg=False):
    global logger
    logger = logging.getLogger('pyhera')
    logger.setLevel(logging.DEBUG if dbg else logging.INFO)

    global logHandle
    logHandle = logging.FileHandler(filename)
    logHandle.setLevel(logging.DEBUG if dbg else logging.INFO)

    formatString = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(formatString)

    logHandle.setFormatter(formatter)
    logger.addHandler(logHandle)

def error(msg):
    global logger
    logger.error(msg)

def info(msg):
    global logger
    logger.info(msg)

def debug(msg):
    global logger
    logger.debug(msg)
