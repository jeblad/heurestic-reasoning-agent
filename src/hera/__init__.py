#
# Distributed according to GNU Affero General Public License v3 Only.
# Copyright (C) 2021, John Erling Blad <jeblad@gmail.com>
#

import locale
import gettext
import os
import os.path
import sys
import importlib
import psutil
from typing import Text
from types import SimpleNamespace
import inspect
import orjson
import hera.logger as logger

__all__ = ['WORKING_DIR', 'LOCALE_DIR', 'PROG_NAME',
    'verbose', 'import_module', 'read_config', 'write_config', 'file_exists']

path = __file__
if os.path.islink(path):
    path = os.readlink(path)

WORKING_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(path)), os.pardir))
LOCALE_DIR = os.path.join(os.path.abspath(os.path.join(WORKING_DIR, os.pardir)), 'locales')

PROG_NAME = 'hera'

locale.setlocale(locale.LC_ALL, '')
gt = gettext.translation(PROG_NAME, localedir=LOCALE_DIR)
_ = gt.gettext
gt.install()

def verbose(level, args=None, config=None):
    if args and args.verbose >= level:
        return lambda msg : print(msg, file=sys.stderr)
    elif config and 'verbose' in config and config['verbose'] >= level:
        return lambda msg : print(msg, file=sys.stderr)
    else:
        return lambda msg: None

def import_module(name, blame, role=None):
    lib = importlib.import_module(".%s" % name, package='pyhera.family')
    if role and not lib:
        raise Exception(_('%s: “%s” has no implementation')%(blame, role))
    return lib

def read_config(filename, blame=None):
    try:
        content = None
        with open(filename, 'rb') as f:
            content = orjson.loads(f.read())
        if content and isinstance(blame, str):
            logger.info(_('%s: config read from file "%s"')%(blame, filename))
        return content or {}
    except Exception as e:
        logger.info(_('%s: %s')%(blame, e))
        return {}

def pid_exists(filename, blame):
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            pid = int(f.read())
            if psutil.pid_exists(pid):
                raise Exception(_('%s: pid file exists (use "down" subcommand to shut down the process)')%(blame))
        return True
    return False

def write_config(filename, data, default=None):
    with open(filename, 'wb') as f:
        if default:
            f.write(orjson.dumps(data, option=orjson.OPT_SERIALIZE_NUMPY, default=default))
        else:
            f.write(orjson.dumps(data, option=orjson.OPT_SERIALIZE_NUMPY))

def dir_exists(path):
    if os.path.isdir(path):
        return path
    return None

def file_exists(path):
    if os.path.isfile(path):
        return path
    return None

def file_available(path):
    if os.path.isfile(path):
        return None
    return path

def called():
    return inspect.stack()[0][3]
