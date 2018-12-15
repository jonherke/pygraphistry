import neo4j


def test_hey():
    driver = neo4j.GraphDatabase.driver("bolt://172.18.0.14:7687", auth=("neo4j", "graphistry"))
    with driver.session() as session:
        statement = session.run(
            """
            MATCH (a)-[r:transaction]->(b) WHERE r.USD > 7000 AND r.USD < 10000  RETURN a, r, b ORDER BY r.USD DESC LIMIT 5
            """,
            {
            }
        )

        graph = statement.graph()

        for relationship in graph.relationships: # type: neo4j.Relationship
            print({
                key: value for key, value in _relahin_fields(node)
            })

        for node in graph.nodes: # type: neo4j.Node
            print({
                key: value for key, value in _node_fields(node)
            })

def _node_fields(node: neo4j.Node):
    yield ("id", node.id)

def _relationship_fields(relationship: neo4j.Relationship):
    yield ("id", relationship.id)