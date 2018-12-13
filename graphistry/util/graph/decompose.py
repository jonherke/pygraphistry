import pyarrow
import os


def decompose(graph):
    for decompose in [_decompose_igraph, _decompose_networkx]:
        try:
            decomposition = decompose(graph)
            if decomposition is not None:
                return decomposition
        except ImportError:
            continue

    raise NotImplementedError()


def _decompose_igraph(graph):
    from graphistry.ext.igraph import to_arrow
    return to_arrow(graph)


def _decompose_networkx(graph):
    from graphistry.ext.networkx import to_arrow
    return to_arrow(graph)
