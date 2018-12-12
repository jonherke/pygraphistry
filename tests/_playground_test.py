import pytest
import graphistry
import networkx
import pyarrow

def test_plot():
    graph = networkx.random_lobster(100, 0.9, 0.9)
    uri = graphistry\
        .data(graph=graph)\
        .bind(
            node_id = graphistry.src.plotter.NODE_ID,
            edge_id = graphistry.src.plotter.EDGE_ID,
            edge_src = graphistry.src.plotter.EDGE_SRC,
            edge_dst = graphistry.src.plotter.EDGE_DST
        )\
        .plot()
    print(uri)
