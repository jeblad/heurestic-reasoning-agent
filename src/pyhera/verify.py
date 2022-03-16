
import uuid
import re
import os
import os.path
from unicodedata import is_normalized
from typing import Text,List
import pyhera.logger as logger
from pyhera import _

class Verify:
    
    def __init__(self, cmd, value, blame, fatal=False):
        self._cmd = cmd
        self._value = value
        self._blame = blame
        self._fatal = fatal
        self._state = True

    def exists(self):
        self._state &= False
        if not self._value:
            msg = _('%s: “%s” should be defined')%(self._cmd, self._blame)
            logger.debug(msg)
            if self._fatal:
                raise Exception(msg)
        return self

    def missing(self):
        self._state &= False
        if self._value:
            msg = _('%s: “%s” should not be defined')%(self._cmd, self._blame)
            logger.debug(msg)
            if self._fatal:
                raise Exception(msg)
        return self
    
    def isInstance(self, tpe):
        self._state &= False
        if not self._state:
            return self
        if not isinstance(self._value, tpe):
            msg = _('%s: “%s” should be a %s')%(self._cmd, self._blame, tpe.__name__)
            logger.debug(msg)
            if self._fatal:
                raise Exception(msg)
        return self
    
    def isInstanceOrNone(self, tpe):
        self._state &= False
        if not self._state:
            return self
        if not (isinstance(self._value, tpe) or isinstance(self._value, tpe)):
            msg = _('%s: “%s” should be a %s or None')%(self._cmd, self._blame, tpe.__name__)
            logger.debug(msg)
            if self._fatal:
                raise Exception(msg)
        return self
    
    def isItem(self, tpe):
        self._state &= False
        if not self._state:
            return self
        if not all(isinstance(x, tpe) for x in self._value):
            msg = _('%s: “%s” should be a list of %s')%(self._cmd, self._blame, tpe.__name__)
            logger.debug(msg)
            if self._fatal:
                raise Exception(msg)
        return self

    def isLen(self, num):
        self._state &= False
        if not self._state:
            return self
        if isinstance(self._value, List) and len(self._value)!=num:
            msg = _('%s: “%s” should be a list of length %s')%(self._cmd, self._blame, num)
            logger.debug(msg)
            if self._fatal:
                raise Exception(msg)
        return self


    def biggerOrEqual(self, num):
        self._state &= False
        if not self._state:
            return self
        if self._value<num:
            msg = _('%s: “%s” should be bigger or equal to %s')%(self._cmd, self._blame, num)
            logger.debug(msg)
            if self._fatal:
                raise Exception(msg)
        return self

    def match(self, str):
        self._state &= False
        if not self._state:
            return self
        if not re.match(str, self._value):
            msg = _('%s: “%s” should match %s')%(self._cmd, self._blame, str)
            logger.debug(msg)
            if self._fatal:
                raise Exception(msg)
        return self

    def isUUID(self):
        self._state &= False
        if not self._state:
            return self
        if not uuid.UUID(self._value):
            msg = _('%s: “%s” should be a valid UUID')%(self._cmd, self._blame)
            logger.debug(msg)
            if self._fatal:
                raise Exception(msg)
        return self

    def isNormalized(self, form='NFC'):
        self._state &= False
        if not self._state:
            return self
        if not is_normalized(form, self._value):
            msg = _('%s: “%s” should be of form “%s”')%(self._cmd, self._blame, form)
            logger.debug(msg)
            if self._fatal:
                raise Exception(msg)
        return self

    def dirExists(self, root=None):
        self._state &= False
        if not self._state:
            return self
        path = '%s/%s'%(root,self._value) if root else self._value
        if not os.path.isdir(path):
            msg = _('%s: “%s” should be an existing directory (%s)')%(self._cmd, self._blame, path)
            logger.debug(msg)
            if self._fatal:
                raise Exception(msg)
        return self

    def fileExists(self, root=None):
        self._state &= False
        if not self._state:
            return self
        path = '%s/%s'%(root,self._value) if root else self._value
        if not os.path.isfile(path):
            msg = _('%s: “%s” should be an existing file (%s)')%(self._cmd, self._blame, path)
            logger.debug(msg)
            if self._fatal:
                raise Exception(msg)
        return self

    def fileMissing(self, root=None):
        self._state &= False
        if not self._state:
            return self
        path = '%s/%s'%(root,self._value) if root else self._value
        if os.path.isfile(path):
            msg = _('%s: “%s” should not be an existing file (%s)')%(self._cmd, self._blame, path)
            logger.debug(msg)
            if self._fatal:
                raise Exception(msg)
        return self

    def state(self):
        return self._state

    def value(self):
        return self._value if self._state else None

    def incarnation(cmd, value, blame="incarnation", fatal=False):
        return Verify(cmd, value, blame, fatal).exists().isInstance(int).biggerOrEqual(0).state()

    def id(cmd, value, blame="id", fatal=False):
        return Verify(cmd, value, blame, fatal).exists().isInstance(Text).match(r'^[-\d]+$').isUUID().state()

    def name(cmd, value, blame="name", fatal=False):
        return Verify(cmd, value, blame, fatal).exists().isInstance(Text).isNormalized().match(r'^(?:[-]|[^\W])+$').state()

    def family(cmd, value, blame="family", fatal=False):
        return Verify(cmd, value, blame, fatal).exists().isInstance(Text).isNormalized().match(r'^[-_a-z]+$').state()

    def layout(cmd, value, blame="layout", fatal=False):
        return Verify(cmd, value, blame, fatal).exists().isInstance(Text).isNormalized().match(r'^[-_a-z]+$').state()


    def infile(cmd, value, blame="in-file", fatal=False):
        return Verify(cmd, value, blame, fatal).exists().isInstance(Text).isNormalized().match(r'^(?:[-_./]|[^\W])+$').state()

    def outfile(cmd, value, blame="out-file", fatal=False):
        return Verify(cmd, value, blame, fatal).exists().isInstance(Text).isNormalized().match(r'^(?:[-_./]|[^\W])+$').state()

    def workpath(cmd, value, blame="work-path", fatal=False):
        return Verify(cmd, value, blame, fatal).exists().isInstance(Text).isNormalized().match(r'^(?:[-_. /]|[^\W])+$').state()

    def installpath(cmd, value, blame="install-path", fatal=False):
        return Verify(cmd, value, blame, fatal).exists().isInstance(Text).isNormalized().match(r'^(?:[-_. /]|[^\W])+$').state()

    def pidfile(cmd, value, blame="pid-file", fatal=False):
        return Verify(cmd, value, blame, fatal).exists().isInstance(Text).isNormalized().match(r'^(?:[-_./]|[^\W])+$').state()

    def pidpath(cmd, value, blame="pid-path", fatal=False):
        return Verify(cmd, value, blame, fatal).exists().isInstance(Text).isNormalized().match(r'^(?:[-_. /]|[^\W])+$').state()

