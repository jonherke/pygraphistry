import neo4j
import pyarrow as arrow
import itertools

from graphistry.plotter import NODE_ID, EDGE_ID, EDGE_SRC, EDGE_DST

def to_arrow( # TODO(cwharris): move these consts out of here
    graph,
    node_id_column_name=NODE_ID,
    edge_id_column_name=EDGE_ID,
    edge_src_column_name=EDGE_SRC,
    edge_dst_column_name=EDGE_DST,
    neo4j_type_column_name="__NEO4J_TYPE__",
    neo4j_label_column_name="__NEO4J_LABEL__"
):
    edge_table = _edge_table(
        graph.relationships
    )

    node_table = _node_table(
        graph.nodes
    )

    return (edge_table, node_table)

def _edge_table(relationships):
    attribute_names = _attributes_for_entities(relationships)
    return arrow.Table.from_arrays(
        [column for column in itertools.chain(
            _intrinsic_edge_columns(relationships),
            _columns_for_entity(relationships, attribute_names)
        )]
    )

def _node_table(nodes):
    attribute_names = _attributes_for_entities(nodes)
    return arrow.Table.from_arrays(
        [column for column in itertools.chain(
            _intrinsic_node_columns(nodes),
            _columns_for_entity(nodes, attribute_names)
        )]
    )

def _attributes_for_entities(entities):
    return set(
        key for entity in entities for key in entity.keys()
    )

def _columns_for_entity(entities, entity_attributes):
    for attribute in entity_attributes:
        yield arrow.column(attribute, [
            [entity[attribute] if attribute in entity else None for entity in entities]
        ])

def _intrinsic_edge_columns(relationships):
    yield arrow.column(EDGE_ID, [
        [relationship.id for relationship in relationships]
    ])

    yield arrow.column(EDGE_SRC, [
        [relationship.start_node.id for relationship in relationships]
    ])

    yield arrow.column(EDGE_DST, [
        [relationship.end_node.id for relationship in relationships]
    ])

    yield arrow.column("__NEO4J_TYPE__", [
        [relationship.type for relationship in relationships]
    ])

def _intrinsic_node_columns(nodes):
    yield arrow.column(NODE_ID, [
        [node.id for node in nodes]
    ])

    yield arrow.column("__NEO4J_LABELS__", [
        [list(node.labels) for node in nodes]
    ])

# def _node_fields(  # TODO(cwharris) make keys configurable
#     node: neo4j.Node,
#     node_id_column_name: str,
#     neo4j_label_column_name: str
# ):
#     yield (node_id_column_name, node.id)
#     yield (neo4j_label_column_name, node.labels)
#     for item in node.items():
#         yield item

# def _relationship_fields( # TODO(cwharris) make keys configurable
#     relationship: neo4j.Relationship,
#     edge_id_column_name: str,
#     edge_src_column_name: str,
#     edge_dst_column_name: str,
#     neo4j_type_column_name: str
# ):
#     yield (edge_id_column_name, relationship.id)
#     yield (edge_src_column_name, relationship.start_node.id)
#     yield (edge_dst_column_name, relationship.end_node.id)
#     yield (neo4j_type_column_name, relationship.type)

#     for item in relationship.items():
#         yield item