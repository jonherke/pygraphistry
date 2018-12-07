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
    import igraph
    if not isinstance(graph, igraph.Graph):
        return None
    raise NotImplementedError()


def decompose_networkx(graph):
    import networkx
    if not isinstance(graph, networkx.Graph):
        return None
    raise NotImplementedError()
