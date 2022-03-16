"""The down subcommand."""

#
# Distributed according to GNU Affero General Public License v3 Only.
# Copyright (C) 2021, John Erling Blad <jeblad@gmail.com>
#

import argparse
from pyhera import _

class Subcmd:
    def __init__(self, subcommand):
        self.subcommand = subcommand

    def __call__(self, args):
        print('executing %s'%self)

    def __repr__(self):
        return '<cmd> %s'%self.subcommand

    def make_subparser(self, parser):
        self.parser = parser.add_parser(self.subcommand,
            help=_('stop and unload an agent'),
            description=_('Stop and unload the agent'))
        self.parser.set_defaults(action=self)

