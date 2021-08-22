"""The layouts subcommand."""

#
# Distributed according to Norwegian Copyright law.
# Copyright (C) 2021, John Erling Blad <jeblad@gmail.com>
#

# standard libs
# import argparse
import pkgutil
import re

from pyhera import _

_exclude_pattern = re.compile(r'\/__.+__\.py$')

class Layouts:
    def __init__(self, subcommand):
        self.subcommand = subcommand

    def __call__(self, args):
        print('executing %s'%self)

    def __repr__(self):
        return '<cmd> %s'%self.subcommand

    def make_subparser(self, parser):
        self.parser = parser.add_parser(self.subcommand,
            help=_('list all available layouts'),
            description=_('List all available layouts'))
        self.parser.add_argument('-l', '--layout',
            type=str,
            help=_('list only this layout name'))
        self.parser.set_defaults(action=self)
