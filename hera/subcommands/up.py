"""The up subcommand."""

#
# Distributed according to Norwegian Copyright law.
# Copyright (C) 2021, John Erling Blad <jeblad@gmail.com>
#

import argparse
from hera import _

class Up:
    def __init__(self, subcommand):
        self.subcommand = subcommand

    def __call__(self, args):
        print('executing %s'%self)

    def __repr__(self):
        return '<cmd> %s'%self.subcommand

    def make_subparser(self, parser):
        self.parser = parser.add_parser(self.subcommand,
            help=_('load and start an agent'),
            description=_('Load and start the agent'))
        self.parser.add_argument('--daemonize',
            action='store_true',
            help=_('run as daemon if possible (abort on command mode)'))
        self.parser.add_argument('--check',
            action='store_true',
            help=_('check if the agent loads, and then abort'))
        self.parser.add_argument('-c', '--command',
            action='store_true',
            help=_('open command mode'))
        self.parser.add_argument('-s', '--singlestep',
            nargs='?',
            type=int,
            help=_('one or N single steps in command mode'))
        self.parser.add_argument('--device',
            type=int,
            help=_('index for device to populate'))
        self.parser.set_defaults(action=self)
