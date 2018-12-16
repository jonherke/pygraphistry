import neo4j
import itertools

def test_hey():
    driver = neo4j.GraphDatabase.driver("bolt://neo4j:7687")
    # MATCH (a)-[r:TRANSACTION]->(b) WHERE r.USD > 7000 AND r.USD < 10000  RETURN a, r, b ORDER BY r.USD DESC LIMIT 5
    with driver.session() as session:
        statement = session.run("MATCH (a)-[r:TRANSACTION]->(b) RETURN a, r, b LIMIT 1", { })

        graph = statement.graph()

        for relationship in graph.relationships: # type: neo4j.Relationship
            print(json.dumps({
                key: value for key, value in _relationship_fields(relationship)
            }, indent=4))

        for node in graph.nodes: # type: neo4j.Node
            print(json.dumps({
                key: value for key, value in _node_fields(node)
            }, indent=4))
        
        

def _node_fields(node: neo4j.Node): # TODO(cwharris) make keys configurable
    yield ("__NODE_ID__", node.id)
    yield ("__NEO4J_LABEL__", node.labels)
    for item in node.items():
        yield item

def _relationship_fields(relationship: neo4j.Relationship): # TODO(cwharris) make keys configurable
    yield ("__EDGE_ID__", relationship.id)
    yield ("__EDGE_SRC__", relationship.start_node.id)
    yield ("__EDGE_DST__", relationship.end_node.id)
    yield ("__NEO4J_TYPE__", relationship.type)
    for item in relationship.items():
        yield item
