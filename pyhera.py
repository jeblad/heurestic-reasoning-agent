#!/usr/bin/env python3

#
# Distributed according to Norwegian Copyright law.
# Copyright (C) 2021, John Erling Blad <jeblad@gmail.com>
#

# standard libs
import argparse

# third party libs

# local libs
from pyhera import *
from pyhera import _

from pyhera.build import Build
from pyhera.destroy import Destroy
from pyhera.up import Up
from pyhera.down import Down
from pyhera.agents import Agents
from pyhera.devices import Devices
from pyhera.types import Types
from pyhera.layouts import Layouts

commands = []
commands.append(Build('build'))
commands.append(Destroy('destroy'))
commands.append(Up('up'))
commands.append(Down('down'))
commands.append(Agents('agents'))
commands.append(Devices('devices'))
commands.append(Types('types'))
commands.append(Layouts('layouts'))

def main():
    # top-level parser
    parser = argparse.ArgumentParser(
        prog=PROG_NAME,
        description=_('Heuristic Reasoning Agent – a service and a daemon for simple AI tasks.'),
        epilog=_('For further help, check the documentation.'))
    parser.add_argument('--simulate', '-s',
        action='store_true',
        help=_('calculate and allocate, but do not load'))
    parser.add_argument('--verbose', '-v',
        action='count',
        default=0,
        help=_('turn on increasing verbose mode'))
    parser.add_argument('-n', '--name',
        type=str,
        help=_('name for the specific agent'))
    parser.add_argument('-i', '--identifier',
        type=str,
        help=_('identifier for the specific agent'))
    parser.add_argument('--force',
        action='store_true',
        help=_('continue without asking'))

    subparsers = parser.add_subparsers(title=_('subcommands'),
        description=_('valid subcommands'),
        help=_('help for subcommands'),
        required=True)

    # parsers for subcommands
    for cmd in commands:
        cmd.make_subparser(subparsers)

    args = parser.parse_args()
    args.action(args)


if __name__ == '__main__':
    main()
