import pyarrow
import os


def decompose(graph):
    for decomposer in [_decompose_igraph, _decompose_networkx]:
        try:
            decomposition = decomposer(graph)
            if decomposition is None:
                continue
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
