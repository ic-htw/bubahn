
import pandas as pd
from neo4j import GraphDatabase
import cred as c

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

# 2860664: messages
# 1121226: posts
# 1739438: comments
q = "MATCH (x) return labels(x), count(*)"
with GraphDatabase.driver(c.neo4j_host, auth=(c.neo4j_userid, c.neo4j_password)) as driver:
    with driver.session() as session:
        result = session.run(q, person1Id=100, person2Id=563)
        df = pd.DataFrame(result.data())
print(df)

q = "MATCH (x)-[r]->(y) return labels(x), type(r), labels(y), count(*)"
with GraphDatabase.driver(c.neo4j_host, auth=(c.neo4j_userid, c.neo4j_password)) as driver:
    with driver.session() as session:
        result = session.run(q, person1Id=100, person2Id=563)
        df = pd.DataFrame(result.data())

print(df)

# with GraphDatabase.driver(c.neo4j_host, auth=(c.neo4j_userid, c.neo4j_password)) as driver:
#     q = f"MATCH (x:Tag) return count(*);"
#     rel = "(x:Comment)-[z:REPLY_OF]->(y:Message)"
#     q = f"MATCH {rel} return count(*);"
#     with driver.session() as session:
#         rs = session.run(q)
#         df = pd.DataFrame(rs.data())
#     print(df)
    

