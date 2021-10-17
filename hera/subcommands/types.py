"""The types subcommand."""

#
# Distributed according to Norwegian Copyright law.
# Copyright (C) 2021, John Erling Blad <jeblad@gmail.com>
#

# standard libs
# import argparse
import importlib.resources
import ast
import pkgutil
import re

from hera import _

_exclude_pattern = re.compile(r'\/__.+__\.py$')

class Types:
    def __init__(self, subcommand):
        self.subcommand = subcommand

    def __call__(self, args):
        for filename in importlib.resources.files('pyhera.type').glob('*.py'):
            if re.match(_exclude_pattern, filename.as_posix()):
                continue
            with open(filename, 'r') as file:
                data = ast.parse(file.read())
                if data != None:
                    doc = ast.get_docstring(data)
                    if doc != None:
                        print(ast.get_docstring(data))

    def __repr__(self):
        return '<cmd> %s'%self.subcommand

    def make_subparser(self, parser):
        self.parser = parser.add_parser(self.subcommand,
            help=_('list all available types'),
            description=_('List all available types'))
        self.parser.add_argument('-t', '--type',
            type=str,
            help=_('list only this type name'))
        self.parser.set_defaults(action=self)
