"""The install subcommand."""

#
# Distributed according to Norwegian Copyright law.
# Copyright (C) 2021, John Erling Blad <jeblad@gmail.com>
#

import os
import os.path
from typing import Text
import hera
from hera import verify as verify
from hera import _
import hera.logger as logger

class Install:
    def __init__(self, subcommand=None):
        self.subcommand = subcommand or __class__.__name__.lower()

    def __call__(self, args):
        logger.debug(_('%s: reading config…')%(self.subcommand))

        opts = hera.read_config('./pyhera.json') | hera.read_config('~/.pyhera')
        opts |= {k: v for k, v in vars(args).items() if v is not None}
        opts |= opts.pop('up', {})

        work_path = None
        if verify.workpath(self.subcommand, opts, 'work-path', fatal=False):
            work_path = work_path or hera.dir_exists(opts['work-path'])
        if not work_path:
            raise Exception(_('%s: can not locate local work directory')%(self.subcommand))
        
        infile = None
        if not verify.infile(self.subcommand, opts, 'in-file', fatal=False):
            infile = infile or hera.file_exists('%s/%s'%(work_path, opts['in-file']))
        if not verify.name(self.subcommand, opts, 'name', fatal=False):
            infile = infile or hera.file_exists('%s/%s'%(work_path, '%s.json' % opts['name']))
        if not verify.id(self.subcommand, opts, 'id', fatal=False):
            infile = infile or hera.file_exists('%s/%s'%(work_path, '%s.json' % opts['id']))
        if not infile:
            raise Exception(_('%s: can not locate infile')%(self.subcommand))
        
        config = hera.read_config(infile)

        verify.name(self.subcommand, config, 'name', fatal=True)
        if 'name' in opts and opts['name'] != config['name']:
            raise Exception(_('%s: “name” is inconsistent')%(self.subcommand))
        
        verify.id(self.subcommand, config, 'id', fatal=True)
        if 'id' in opts and opts['id'] != config['id']:
            raise Exception(_('%s: “id” is inconsistent')%(self.subcommand))
        
        verify.pidpath(self.subcommand, opts, 'pid-path', fatal=True)
        verify.pidfile(self.subcommand, opts, 'pid-file', fatal=False)
        pid_file = '%s/%s'%(opts['pid-path'], opts['pid-file'] % config['id'])
        # this could happen due to user error
        if os.path.isfile(pid_file):
            if hera.pid_exists(pid_file):
                raise Exception(_('%s: pid file exists (use "down" subcommand to shut down the process)')%(self.subcommand))
            if opts['force']:
                os.unlink(pid_file)
            else:
                raise Exception(_('%s: pid file exists (use "--force" to override)')%(self.subcommand))

        install_path = None
        verify.installpath(self.subcommand, opts, 'install-path', fatal=True)
        install_path = install_path or hera.dir_exists(opts['install-path'])
        if not install_path:
            raise Exception(_('%s: can not locate install directory')%(self.subcommand))

        outfile = '%s/%s.json'%(install_path, config['id'])
        if os.path.isfile(outfile):
            if opts['force']:
                os.unlink(pid_file)
            else:
                raise Exception(_('%s: install file with same name exists (use "--force" to override)')%(self.subcommand))
 
        logger.debug(_('%s: installing config for brain…')%(self.subcommand))
        hera.write_config(outfile, config)
        logger.debug(_('%s: config installed to file "%s"')%(self.subcommand, outfile))
        if not opts['silent']:
            print(_('%s: config installed to file "%s"')%(self.subcommand, outfile))

    def __repr__(self):
        return '<cmd> %s'%self.subcommand

    def make_subparser(self, parser):
        self.parser = parser.add_parser(self.subcommand,
            help=_('install a copy of an agent (does not delete the local copy)'),
            description=_('Install the copy of an agent'))
        self.parser.set_defaults(action=self)

