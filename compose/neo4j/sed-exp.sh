cat ./compose/neo4j/edges.csv \
    | sed -E "s/([a-z0-9]{32})\.\.\./\1/g" \
    | sed -E "s/([a-z0-9]{32})([a-z0-9]{8})/\1/g" \
    | sed "s/2a37b3bdca935152335c2097e5da367d/Ross Ulbricht (SilkRoad)/g" \
    | sed "s/b2233dd22ade4c9978ec1fd1fbb36eb7/Carl Force (DEA)/g" \
    > ./compose/neo4j/edges-edited.csv

cat ./compose/neo4j/nodes.csv \
    | sed -E "s/([a-z0-9]{32})\.\.\./\1/g" \
    | sed -E "s/([a-z0-9]{32})([a-z0-9]{8})/\1/g" \
    | sed "s/2a37b3bdca935152335c2097e5da367d/Ross Ulbricht (SilkRoad)/g" \
    | sed "s/b2233dd22ade4c9978ec1fd1fbb36eb7/Carl Force (DEA)/g" \
    > ./compose/neo4j/nodes-edited.csv
