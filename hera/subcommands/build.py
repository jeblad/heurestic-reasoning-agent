"""The build subcommand."""

#
# Distributed according to GNU Affero General Public License v3 Only.
# Copyright (C) 2021, John Erling Blad <jeblad@gmail.com>
#

import os
from unicodedata import is_normalized

import uuid
from typing import Text

import hera
import hera.name as name
from hera.verify import Verify as makeVerify
import hera.logger as logger
from hera import _

class Build:
    def __init__(self, subcommand=None):
        self.subcommand = subcommand or __class__.__name__.lower()

    def __call__(self, args):
        logger.debug(_('%s: started')%(self.subcommand))

        opts = {}
        opts |= hera.read_config('./pyhera.json', self.subcommand)
        opts |= hera.read_config('~/.pyhera', self.subcommand)
        opts |= {k.replace('_', '-'): v for k, v in vars(args).items() if v is not None}
        opts |= opts.pop('build', {})

        work_path = makeVerify(self.subcommand, opts['work-path'] if 'work-path' in opts else None, 'work-path', True) \
            .exists().isInstance(Text).isNormalized().match(r'^(?:[-_. /]|[^\W])+$').dirExists().value()

        install_path = makeVerify(self.subcommand, opts['install-path'] if 'install-path' in opts else None, 'install-path', True) \
            .exists().isInstance(Text).isNormalized().match(r'^(?:[-_. /]|[^\W])+$').dirExists().value()

        infile = makeVerify(self.subcommand, opts['in-file'] if 'in-file' in opts else None, 'in-file', False) \
            .exists().isInstance(Text).isNormalized().match(r'^(?:[-_./]|[^\W])+$').fileExists(work_path).value() \

        if not infile:
            if opts['force'] <= 0:
                raise Exception(_('%s: can not construct a valid input filename (use or increment “--force” to override)')%(self.subcommand))
            opts['force'] -= 1

        layout = makeVerify(self.subcommand, opts['layout'] if 'layout' in opts else None, 'layout', False) \
            .exists().isInstance(Text).isNormalized().match(r'^[-_a-z0-9]+$').value()
        if layout:
            config = hera.read_config('%s/layout/%s'%(install_path, '%s.json' % layout), self.subcommand)
        
        config |= opts
        if infile:
            fullpath = '%s/%s'%(work_path, infile)
            if not opts['silent']:
                print(_('%s: reading config from file "%s"')%(self.subcommand, fullpath))
            config |= hera.read_config(fullpath)
        
        incarnation = makeVerify(self.subcommand, config['incarnation'] if 'incarnation' in config else None, 'incarnation', False) \
            .exists().state()
        if incarnation:
            raise Exception(_('%s: got configuration of an existing agent')%(self.subcommand))
           
        config['incarnation'] = 0

        if not 'id' in config:
            config['id'] = str(uuid.uuid4())
        
        makeVerify(self.subcommand, config['id'] if 'id' in config else None, 'id', True) \
            .exists().isInstance(Text).isUUID()

        if not 'name' in config:
            config['name'] = name.get(config['id'], config.get('gender', None))
        makeVerify(self.subcommand, config['name'] if 'name' in config else None, 'name', True) \
            .exists().isInstance(Text).isNormalized().match(r'^(?:[-]|[^\W])+$')

        makeVerify(self.subcommand, config['family'] if 'family' in config else None, 'family', True) \
            .exists().isInstance(Text).isNormalized().match(r'^[-_a-z]+$')

        pid_path = makeVerify(self.subcommand, opts['pid-path'] if 'pid-path' in opts else None, 'pid-path', True) \
            .exists().isInstance(Text).isNormalized().match(r'^(?:[-_. /]|[^\W])+$').dirExists().value()

        pid_format = makeVerify(self.subcommand, opts['pid-file'] if 'pid-file' in opts else None, 'pid-file', True) \
            .exists().isInstance(Text).isNormalized().match(r'^(?:[-_. /%]|[^\W])+$').value()

        pid_file = '%s/%s'%(pid_path, pid_format % config['id'])
        if hera.pid_exists(pid_file, self.subcommand):
            if opts['force'] <= 0:
                raise Exception(_('%s: pid file exists (use "--force" to override)')%(self.subcommand))
            opts['force'] -= 1
            os.unlink(pid_file)

        family = hera.import_module(config['family'], self.subcommand, 'family')
        brain = family.build(config)

        outfile = makeVerify(self.subcommand, opts['out-file'] if 'out-file' in opts else None, 'out-file', False) \
            .exists().isInstance(Text).isNormalized().match(r'^(?:[-_./]|[^\W])+$').fileMissing(work_path).value() \
            or makeVerify(self.subcommand, ('%s.json'%(config['id'])) if 'id' in config else None, 'id', False) \
            .exists().isInstance(Text).isNormalized().match(r'^(?:[-_./]|[^\W])+$').fileMissing(work_path).value()

        if not outfile:
            raise Exception(_('%s: can not construct a valid output filename')%(self.subcommand))

        hera.write_config('%s/%s'%(work_path, outfile), brain, family.default)

        if not opts['silent']:
            print(_('%s: config written to file "%s/%s"')%(self.subcommand, work_path, outfile))

        logger.debug(_('%s: ended')%(self.subcommand))

    def __repr__(self):
        return '<cmd> %s'%self.subcommand

    def make_subparser(self, parser):
        self.parser = parser.add_parser(self.subcommand,
            help=_('build an agent'),
            description=_('Build the agent, but do not load or run it'))
        self.parser.add_argument('-f', '--family',
            type=str,
            help=_('family name for the agent'))
        self.parser.add_argument('-l', '--layout',
            type=str,
            help=_('layout name for the agent'))
        self.parser.add_argument('-d', '--description',
            type=str,
            help=_('layout name for the agent'))
        self.parser.set_defaults(action=self)
