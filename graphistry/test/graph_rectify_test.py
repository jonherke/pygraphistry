import random
import string

import pyarrow as arrow
import pytest

from graphistry.src import graph_rectify

int32 = arrow.int32()

id_column_name = 'ids'
letters_column_name = 'letters'


def test_rectify_edge_ids_int64():
    edge_table = _create_simple_table()
    edge_table = graph_rectify.rectify_edge_ids(
        edge_table,
        id_column_name
    )
    assert edge_table.column(id_column_name).type == int32


def test_rectify_edge_ids_string():
    edge_table = _create_simple_table()
    edge_table = graph_rectify.rectify_edge_ids(
        edge_table,
        letters_column_name
    )
    assert edge_table.column(letters_column_name).type == int32


def test_rectify_edge_ids_missing():
    edge_table = _create_simple_table()
    edge_table = graph_rectify.rectify_edge_ids(
        edge_table,
        'letter'
    )
    assert edge_table.column(letters_column_name).type == int32


def test_rectify_node_ids():
    pass


def _create_simple_table() -> arrow.Table:
    letters = arrow.column(
        letters_column_name, [string.ascii_uppercase])
    indicies = arrow.column(
        id_column_name, [range(letters.length())])
    return arrow.Table.from_arrays([
        indicies,
        letters
    ])
