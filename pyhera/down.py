"""The down subcommand."""

#
# Distributed according to Norwegian Copyright law.
# Copyright (C) 2021, John Erling Blad <jeblad@gmail.com>
#

import argparse
from pyhera import _

class Down:
    def __init__(self, subcommand):
        # initialize stuff
        self.subcommand = subcommand

    def __call__(self, args):
        # do stuff when subcommand is called
        print('executing %s'%self)

    def __repr__(self):
        # make a representation of the object
        return '<cmd> %s'%self.subcommand

    def make_subparser(self, parser):
        self.parser = parser.add_parser(self.subcommand,
            help=_('stop and unload an agent'),
            description=_('Stop and unload the agent'))
        self.parser.set_defaults(action=self)

