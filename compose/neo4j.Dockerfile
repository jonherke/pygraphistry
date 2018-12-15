FROM neo4j:3.5
COPY ./compose/neo4j-data/nodes-edited.csv /opt/neo4j-data/nodes.csv
# COPY ./compose/neo4j-data/edges.csv /opt/neo4j-data/edges.csv
COPY ./compose/neo4j-data/edges-edited.csv /opt/neo4j-data/edges.csv
RUN neo4j-admin import \
    --nodes /opt/neo4j-data/nodes.csv \
    --relationships /opt/neo4j-data/edges.csv
