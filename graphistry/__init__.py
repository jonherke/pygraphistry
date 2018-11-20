from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from graphistry.plotter import Plotter

def data(**data):
    return Plotter(data = data)

def bind(**bindings):
    return Plotter(bindings = bindings)

def settings(**bindings):
    return Plotter(settings = settings)