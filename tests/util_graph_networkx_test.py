import pytest
import networkx

from graphistry.src import util_graph_networkx


def test_to_arrow():
    graph = networkx.random_lobster(100, 0.9, 0.9)
    (edges, nodes) = util_graph_networkx.to_arrow(graph)
    assert len(graph.nodes()) == len(nodes)
    assert len(graph.edges()) == len(edges)
    pass

if __name__ == '__main__':
    pytest.main()
