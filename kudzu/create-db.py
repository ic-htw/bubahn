import kuzu

db = kuzu.database('./bubahn.kuzu')
con = kuzu.connection(db)

# -------------------------------------------------
# haltestelle
# -------------------------------------------------
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
# con.execute(q)

# -------------------------------------------------
# segment
# -------------------------------------------------
q = """
create rel table segment (
    from haltestelle to haltestelle,
    laenge_in_meter  int64
);
"""
con.execute(q)

q = """
copy segment from '../csv/segment.csv' (HEADER=true);
"""
con.execute(q)

print('ok')