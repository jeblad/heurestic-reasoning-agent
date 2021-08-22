"""The "abraxas" module for yaml configuation"""

# TODO: replace yaml with json

import yaml
import re
import inspect

def findParent(obj, cls):
    while not isinstance(obj, cls):
        if not hasattr(obj, 'parent'):
            return None
        obj = obj.parent
    return obj

class Error(Exception):
    """Base class for exceptions in abraxas."""
    pass

class ChangeError(Error):
    """Exception raised while trying to change an already created brain.

    Attributes:
        tag -- the tag where the error occured
        message -- a description of the error
    """

    def __init__(self, tag, message):
        self.tag =tag
        self.message = message

class InconsistentError(Error):
    """Exception raised when something is inconsistent during construction of a brain.

    Attributes:
        tag -- the tag where the error occured
        message -- a description of the error
    """

    def __init__(self, tag, message):
        self.tag =tag
        self.message = message

class Brain(yaml.YAMLObject):
    yaml_tag = u'!Brain'

    def __init__(self, name=None, id=None, description=None, neos=None):
        self.name = name if name != None else ''
        self.id = id if id != None else 0
        self.description = description if description != None else ''
        self.neos = neos if neos != None else []
    
    def __setstate__(self, data):
        self.__init__(**data)
    
    def __repr__(self):
        return "%s(name=%r, id=%r, description=%r, neos=%r" % (
            self.__class__.__name__,
            self.name,
            self.id,
            self.description,
            self.neos)

    def build(self):
        for neo in self.neos:
            neo.build(self)
        return self


class Neo(yaml.YAMLObject):
    yaml_tag = u'!Neo'

    def __init__(self, index=None, grid=None, block=None, depth=None, layers=None):
        self.index = index
        self.grid = grid if grid != None else Dim2(32, 32)
        self.block = block if block != None else Dim2(2, 16)
        self.depth = depth if depth != None else Dim1(6)
        self.layers = layers if layers != None else []

    def __setstate__(self, data):
        self.__init__(**data)

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['parent']
        return state

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['parent']
        return state
    
    def __repr__(self):
        return "%s(index=%r, grid=%r, block=%r, depth=%r, layers=%r" % (
            self.__class__.__name__,
            self.index,
            self.grid,
            self.block,
            self.depth,
            self.layers)

    def build(self, parent):
        self.parent = parent
        if len(self.layers) > 0 and len(self.layers) != self.depth:
            raise ChangeError(self.yaml_tag, 'found inconsistent number of items in layers')
        self.layers = [NeoLayer().build(self) for i in range(self.depth[0])]
        return self

class NeoLayer(yaml.YAMLObject):
    yaml_tag = u'!NeoLayer'

    def __init__(self, columns=None, mixins=None):
        self.columns = columns if columns != None else []
        self.mixins = mixins if mixins != None else []
    
    def __setstate__(self, data):
        self.__init__(**data)

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['parent']
        return state
    
    def __repr__(self):
        return "%s(columns=%r, mixins=%r, " % (
            self.__class__.__name__,
            self.columns,
            self.mixins)

    def build(self, parent):
        self.parent = parent
        if len(parent.block) == 3:
            self.columns = [SuperColumn().build(self) for i in range(parent.block[0])]
        elif len(parent.block) == 2:
            self.columns = [MacroColumn().build(self) for i in range(parent.block[0])]
        else:
            raise TypeError
        return self

class SuperColumn(yaml.YAMLObject):
    """A supercolumn is multiple multidimensional lines on the hyperdimensional manifold
    
    It is a container for a set of macrocolumns, thus it forms several directed point clouds.
    Each macrocolumn within a supercolumn observe the same part of assoc through its aperture.
    A supercolumn can be simplified with some loss of information."""

    yaml_tag = u'!SuperColumn'
    
    def __init__(self, columns=None):
        self.columns = columns if columns != None else []

    def __setstate__(self, data):
        self.__init__(**data)

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['parent']
        return state
    
    def __repr__(self):
        return "%s(columns=%r" % (
            self.__class__.__name__,
            self.columns)

    def build(self, parent):
        self.parent = parent
        neo = findParent(self, Neo)
        if neo == None:
            raise InconsistentError()
        self.columns = [MacroColumn().build(self) for i in range(neo.block[1])]
        return self


class MacroColumn(yaml.YAMLObject):
    """A macrocolumn is a multidimensional line on the hyperdimensional manifold

    It is a container for a set of microcolumns, thus it forms a directed point cloud.
    Each microcolumn within a macrocolumn observe the same part of assoc through its aperture.
    A macrocolumn can be simplified with some loss of information."""

    yaml_tag = u'!MacroColumn'
    
    def __init__(self, columns=None):
        self.columns = columns if columns != None else []

    def __setstate__(self, data):
        self.__init__(**data)

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['parent']
        return state
    
    def __repr__(self):
        return "%s(columns=%r" % (
            self.__class__.__name__,
            self.columns)

    def build(self, parent):
        self.parent = parent
        neo = findParent(self, Neo)
        if neo == None:
            raise InconsistentError()
        #self.columns = [MicroColumn().build(self) for i in range(neo.block[-2])]
        return self

class MicroColumn(yaml.YAMLObject):
    """A microcolumn is a multidimensional point on the hyperdimensional manifold
    
    """
    yaml_tag = u'!MicroColumn'
    
    def __init__(self, neurons=None):
        self.neurons = neurons if neurons != None else []

    def __setstate__(self, data):
        self.__init__(**data)

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['parent']
        return state
    
    def __repr__(self):
        return "%s(neurons=%r" % (
            self.__class__.__name__,
            self.neurons)

    def build(self, parent):
        self.parent = parent
        neo = findParent(self, Neo)
        if neo == None:
            raise InconsistentError()
        #self.neurons = [PyramidalNeuron().build(self) for i in range(neo.block[-1])]
        return self

class PyramidalNeuron(yaml.YAMLObject):
    yaml_tag = u'!PyramidalNeuron'
    
    def __init__(self, synapses=None):
        self.synapses = synapses if synapses != None else []

    def __setstate__(self, data):
        self.__init__(**data)
    
    def __repr__(self):
        return "%s(synapses=%r" % (
            self.__class__.__name__,
            self.synapses)

    def build(self, parent):
        self.parent = parent
        return self


class Synapse(tuple):
    def __new__(cls, a, b):
        # It would probably be wrong to use an immutable object here
        return tuple.__new__(cls, [a, b])

    def __repr__(self):
        return "Synapse(%s,%s" % self

def synapse_representer(dumper, data):
    return dumper.represent_scalar(u'!synapse', u'%ss%s' % data)

def synapse_constructor(loader, node):
    value = loader.construct_scalar(node)
    a, b = map(int, value.split('s'))
    return Synapse(a, b)

yaml.add_representer(Synapse, synapse_representer)
yaml.add_constructor(u'!synapse', synapse_constructor)
yaml.add_implicit_resolver(u'!synapse', re.compile(r'^\d+s\d+$'))

class Dim3(tuple):
    def __new__(cls, x, y, z):
        return tuple.__new__(cls, [x, y, z])

    def __repr__(self):
        return "Dim3(%s,%s,%s" % self

    def product(self, count=None):
        if count == None:
            return self[0] * self[1] * self[2]
        elif 0 <= count and count < len(self):
            prod = 1
            for i in range(count):
                prod *= self[i]
            return prod
        else:
            raise ValueError()

def dim3_representer(dumper, data):
    return dumper.represent_scalar(u'!dim3', u'd%s/%s/%s' % data)

def dim3_constructor(loader, node):
    value = loader.construct_scalar(node)
    x, y, z = map(int, value.lstrip('d').split('/'))
    return Dim3(x, y, z)

yaml.add_representer(Dim3, dim3_representer)
yaml.add_constructor(u'!dim3', dim3_constructor)
yaml.add_implicit_resolver(u'!dim3', re.compile(r'^d\d+\/\d+\/\d+$'))

class Dim2(tuple):
    def __new__(cls, x, y):
        return tuple.__new__(cls, [x, y])

    def __repr__(self):
        return "Dim2(%s,%s" % self

    def product(self, count=None):
        if count == None:
            return self[0] * self[1]
        elif 0 <= count and count < len(self):
            prod = 1
            for i in range(count):
                prod *= self[i]
            return prod
        else:
            raise ValueError()

def dim2_representer(dumper, data):
    return dumper.represent_scalar(u'!dim2', u'd%s/%s' % data)

def dim2_constructor(loader, node):
    value = loader.construct_scalar(node)
    x, y = map(int, value.lstrip('d').split('/'))
    return Dim2(x, y)

yaml.add_representer(Dim2, dim2_representer)
yaml.add_constructor(u'!dim2', dim2_constructor)
yaml.add_implicit_resolver(u'!dim2', re.compile(r'^d\d+\/\d+$'))

class Dim1(tuple):
    def __new__(cls, x):
        return tuple.__new__(cls, [x])

    def __repr__(self):
        return "Dim2(%s" % self

    def product(self, count=None):
        if count == None:
            return self[0]
        elif 0 <= count and count < len(self):
            prod = 1
            for i in range(count):
                prod *= self[i]
            return prod
        else:
            raise ValueError()

def dim1_representer(dumper, data):
    return dumper.represent_scalar(u'!dim1', u'd%s' % data)

def dim1_constructor(loader, node):
    value = loader.construct_scalar(node)
    x = map(int, value.lstrip('d'))
    return Dim1(x)

yaml.add_representer(Dim1, dim1_representer)
yaml.add_constructor(u'!dim1', dim1_constructor)
yaml.add_implicit_resolver(u'!dim1', re.compile(r'^d\d+$'))
