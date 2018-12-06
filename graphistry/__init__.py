from graphistry.src.plotter import Plotter
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


def data(**data):
    return Plotter(data=data)


def bind(**bindings):
    return Plotter(bindings=bindings)


def settings(**bindings):
    return Plotter(settings=settings)
