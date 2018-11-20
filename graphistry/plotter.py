import copy
import pandas
import pyarrow

from graphistry import dict_util
from graphistry import graph_util

class Plotter(object):

        _data = {
            'nodes': None,
            'edges': None
        }

        _bindings = {
            # node : data
            'node_id': None,

            # edge : data
            'edge_id': None,
            'edge_src': None,
            'edge_dst': None,

            # node : visualization
            'node_title': None,
            'node_label': None,
            'node_color': None,
            'node_size': None,

            # edge : visualization
            'edge_title': None,
            'edge_label': None,
            'edge_color': None,
            'edge_weight': None,
        }

        _settings = {
            'height': 100
        }

        def __init__(
            self,
            data = None,
            bindings = None,
            settings = None
        ):
            self._data     = data     or self._data
            self._bindings = bindings or self._bindings
            self._settings = settings or self._settings

        def data(self,  **data):
            if 'graph' in data:
                (edges, nodes) = graph_util.decompose(data['graph'])
                return self.data(
                    edges = edges,
                    nodes = nodes
                )

            if 'edges' in data:
                data['edges'] = table_util.to_arrow(data['edges'])

            if 'nodes' in data:
                data['nodes'] = table_util.to_arrow(data['nodes'])

            return Plotter(
                data = dict_util.assign(self._data, data)
            )

        def bind(self,  **bindings):
            return Plotter(
                bindings = dict_util.assign(self._bindings, bindings)
            )

        def settings(self, **settings):
            return Plotter(
                settings = dict_util.assign(self._settings, settings)
            )

        def nodes(self, nodes):
            return self.data(nodes = nodes)

        def edges(self, edges):
            return self.data(edges = edges)

        def graph(self, graph):
            return self.data(graph = graph)

        def plot(self):
            # verify bindings, convert data, and upload
            # - need src, dst, node columns
            pass
