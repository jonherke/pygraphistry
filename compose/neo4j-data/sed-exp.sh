cat ./compose/neo4j-data/edges.csv \
    | sed -E "s/([a-z0-9]{32})\.\.\./\1/g" \
    | sed -E "s/([a-z0-9]{32})([a-z0-9]{8})/\1/g" \
    | sed "s/2a37b3bdca935152335c2097e5da367d/Ross Ulbricht (SilkRoad)/g" \
    | sed "s/b2233dd22ade4c9978ec1fd1fbb36eb7/Carl Force (DEA)/g" \
    | sed 's/$/,transaction/' \
    | sed '1{s/transaction$/:TYPE/}' \
    > ./compose/neo4j-data/edges-edited.csv

cat ./compose/neo4j-data/nodes.csv \
    | sed -E "s/([a-z0-9]{32})\.\.\./\1/g" \
    | sed -E "s/([a-z0-9]{32})([a-z0-9]{8})/\1/g" \
    | sed "s/2a37b3bdca935152335c2097e5da367d/Ross Ulbricht (SilkRoad)/g" \
    | sed "s/b2233dd22ade4c9978ec1fd1fbb36eb7/Carl Force (DEA)/g" \
    > ./compose/neo4j-data/nodes-edited.csv


    | sed "s/2a37b3bdca935152335c2097e5da367d/Ross Ulbricht (SilkRoad)/g" \
    | sed "s/b2233dd22ade4c9978ec1fd1fbb36eb7/Carl Force (DEA)/g" \
# b2233dd22ade4c9978ec1fd1fbb36eb7f9b4609e : Carl Force (DEA)
# Ross Ulbricht (SilkRoad) : 2a37b3bdca935152335c2097e5da367db24209cc