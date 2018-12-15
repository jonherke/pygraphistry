cat ./compose/neo4j-data/edges.csv \
    | sed -E "s/([a-z0-9]{32})\.\.\./\1/g" \
    | sed -E "s/([a-z0-9]{32})([a-z0-9]{8})/\1/g" \
    | sed 's/$/,transaction/' \
    | sed '1{s/$/:TYPE/}' \
    > ./compose/neo4j-data/edges-edited.csv

cat ./compose/neo4j-data/nodes.csv \
    | sed -E "s/([a-z0-9]{32})\.\.\./\1/g" \
    | sed -E "s/([a-z0-9]{32})([a-z0-9]{8})/\1/g" \
    > ./compose/neo4j-data/nodes-edited.csv
