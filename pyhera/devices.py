"""The devices subcommand."""

#
# Distributed according to Norwegian Copyright law.
# Copyright (C) 2021, John Erling Blad <jeblad@gmail.com>
#

import argparse
from pyhera import _

class Devices:
    def __init__(self, subcommand):
        self.subcommand = subcommand

    def __call__(self, args):
        print('executing %s'%self)

    def __repr__(self):
        return '<cmd> %s'%self.subcommand

    def make_subparser(self, parser):
        self.parser = parser.add_parser(self.subcommand,
            help=_('list all available devices'),
            description=_('List all available devices'))
        self.parser.set_defaults(action=self)
