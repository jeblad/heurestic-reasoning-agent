"""The build subcommand."""

#
# Distributed according to Norwegian Copyright law.
# Copyright (C) 2021, John Erling Blad <jeblad@gmail.com>
#

# standard libs
import importlib
import sys
#import argparse

# third party libs
import yaml
# from yaml import load,dump
try:
    from yaml import CLOADER as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


#local libs
from hera import _

class Build:
    def __init__(self, subcommand):
        self.subcommand = subcommand

    def import_type(self, name):
        try:
            self.types = importlib.import_module(".%s" % name, package='pyhera.type')
        except ImportError:
            print('type not found: %s' % name)

    def import_layout(self, name):
        # TODO: replace yaml with json
        try:
            fs = open('layout/%s.yml' % name, 'r')
            self.layout = yaml.load(fs, Loader=Loader)
        except ImportError:
            print('layout not found: %s' % name)


    def __call__(self, args):
        self.import_type(args.type)
        self.import_layout(args.layout)
        self.brain = self.layout.build()
        print(yaml.dump(self.brain, width=50, indent=4, default_flow_style=None))

    def __repr__(self):
        return '<cmd> %s'%self.subcommand

    def make_subparser(self, parser):
        self.parser = parser.add_parser(self.subcommand,
            help=_('build an agent'),
            description=_('Build the agent, but do not load or run it'))
        self.parser.add_argument('-t', '--type',
            required=True,
            type=str,
            help=_('type name for the agent'))
        self.parser.add_argument('-l', '--layout',
            required=True,
            type=str,
            help=_('layout name for the agent'))
        self.parser.set_defaults(action=self)

    def load(self, stream):
        self.data = yaml.load(stream, Loader=Loader)

    def dump(self ):
        # yaml.dump(self.data, stream)
        pass
    