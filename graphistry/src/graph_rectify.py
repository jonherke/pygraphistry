from typing import Tuple, Union

import pyarrow as arrow

int32 = arrow.int32()
int64 = arrow.int64()

def rectify(
    edges: arrow.Table,
    nodes: arrow.Table,
    node: Union[str, int],
    edge_src: Union[str, int],
    edge_dst: Union[str, int],
    safe: bool = True
) -> Tuple[arrow.Table, arrow.Table]:
    # make sure id columns are int32, which may require us to do one of the following:
    # - down-cast from int64
    # - create index via node column and map src/dst/node to their corrosponding index (dType => int32) 
    # - dictionary encode the column (cant do this yet, as server doesn't support it)
    (node,     node_column)     = _get_index_and_column(nodes, node)
    (edge_src, edge_src_column) = _get_index_and_column(edges, edge_src)
    (edge_dst, edge_dst_column) = _get_index_and_column(edges, edge_dst)

    _assert_column_types_match(node_column, edge_src_column)
    _assert_column_types_match(node_column, edge_dst_column)

    # already good to go.
    if node_column.type == arrow.int32:
        return (edges, nodes)
    
    # convert int64 => int32 if no overflow.
    if node_column.type == arrow.int64:
        edges = edges \
            .set_column(edge_src, edge_src_column.cast(int32, safe = safe)) \
            .set_column(edge_dst, edge_dst_column.cast(int32, safe = safe))

        nodes = nodes \
            .set_column(node, node_column.cast(int32, safe = safe))

        return (edges, nodes)

    # replace existing src/dst/node columns with equivolent indices
    index_lookup    = _index_by_value(node_column)
    edge_src_column = _map_column_to_index(index_lookup, edge_src_column)
    edge_dst_column = _map_column_to_index(index_lookup, edge_dst_column)
    node_column     = _map_column_to_index(index_lookup, node_column)

    edges = edges \
        .set_column(edge_src, edge_src_column) \
        .set_column(edge_dst, edge_dst_column)

    nodes = nodes \
        .set_column(node, node_column)
    
    return (edges, nodes)


def _index_by_value(iterable):
    keys = {}
    for (index, value) in enumerate(iterable):
        keys[value] = index
    return keys


def _map_column_to_index(lookup, column: arrow.Column) -> arrow.Column: 
    indicies = [lookup[value] for value in column]
    return arrow.column(column.name, [indicies]).cast(int32, safe = False)


def _get_index_and_column(table: arrow.Table, i) -> Tuple[int, arrow.Column]:
    index = i if isinstance(i, int) else table.schema.get_field_index(i)
    if index < 0:
        raise Exception('column not found: %s' % i)
    return (index, table.column(index))


def _assert_column_types_match(expected: arrow.Column, actual: arrow.Column):
    if actual.type == expected.type:
        return
    raise Exception(
        'column types mismatch (%s/%s). expected(%s) actual(%s)' % (
            expected.name,
            actual.name,
            expected.type,
            actual.type
        )
    )