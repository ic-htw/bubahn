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
match (h:haltestelle) return h.bez;
"""
pdf = con.execute(q).getAsDF()
print(pdf)

print('ok')