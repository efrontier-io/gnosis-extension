
Current protocol URL at thegraph:

    https://thegraph.com/explorer/subgraph/gnosis/protocol

API should look like this:

    https://api.thegraph.com/subgraphs/name/gnosis/protocol

To regenerate graphql_schema.py:

    python -m sgqlc.introspection --exclude-deprecated --exclude-description https://api.thegraph.com/subgraphs/name/gnosis/protocol graphql_schema.json

    sgqlc-codegen graphql_schema.json graphql_schema.py
