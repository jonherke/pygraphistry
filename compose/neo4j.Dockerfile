FROM neo4j:3.5 AS build

COPY ./compose/neo4j/nodes-edited.csv nodes.csv
COPY ./compose/neo4j/edges-edited.csv edges.csv

RUN echo 'dbms.directories.data=data-persistent' > conf/neo4j.conf

RUN neo4j-admin import \
    --mode csv \
    --nodes:ACCOUNT nodes.csv \
    --relationships:TRANSACTION edges.csv

RUN chown -R neo4j /var/lib/neo4j/data-persistent
