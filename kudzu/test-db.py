import kuzu

db = kuzu.database('./bubahn.kuzu')
con = kuzu.connection(db)

q = """
create node table haltestelle (
    hid int64,
    bez string,
    lat double,
    lng double,
    primary key (hid)
);
"""
# con.execute(q)

q = """
match (h1:haltestelle)-[s:segment*1..2]->(h2:haltestelle)
where h1.hid=10166 
return h1.bez, h2.bez;
"""
pdf = con.execute(q).getAsDF()
print(pdf)

print('ok')