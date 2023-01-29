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
copy haltestelle from '../csv/haltestelle.csv' (HEADER=true);
"""
con.execute(q)

print('ok')