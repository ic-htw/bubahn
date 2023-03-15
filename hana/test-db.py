import duckdb
con = duckdb.connect(database='bubahn.duckdb', read_only=True)
sql = """
select count(*) from halt;
"""
con.execute(sql)
print(con.fetchall())
