#
# Distributed according to Norwegian Copyright law.
# Copyright (C) 2021, John Erling Blad <jeblad@gmail.com>
#

# standard lib
import gettext
import os

# local lib

__all__ = ['WORKING_DIR', 'LOCALE_DIR', 'PROG_NAME']

path = __file__
if os.path.islink(path):
    path = os.readlink(path)

WORKING_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(path)), os.pardir))
LOCALE_DIR = os.path.join(WORKING_DIR, 'locales')

PROG_NAME = 'pyhera'

# get localizable messages
gt = gettext.translation(PROG_NAME, localedir=LOCALE_DIR)
_ = gt.gettext
gt.install()


