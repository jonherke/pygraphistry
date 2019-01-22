from graphistry.plotter import Plotter
from graphistry.util import dict_util
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

__plotter = Plotter()

def register(**settings):
    global __plotter
    __plotter = __plotter.settings(**settings)

def data(**data):
    global __plotter
    return __plotter.data(**data)


def bind(**bindings):
    global __plotter
    return __plotter.bind(**bindings)


def settings(**settings):
    global __plotter
    return __plotter.settings(**settings)
