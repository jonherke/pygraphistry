import pyarrow

def decompose(graph):
    for decomposer in [decompose_igraph, decompose_networkx]:
        try:
            decomposition = decomposer(graph)
            if decomposition is None:
                continue
            return decomposition
        except ImportError:
            continue

    raise NotImplementedError()


def decompose_igraph(graph):
    from graphistry.src import util_graph_igraph
    return util_graph_igraph.to_arrow(graph)


def decompose_networkx(graph):
    from graphistry.src import util_graph_networkx
    return util_graph_networkx.to_arrow(graph)
