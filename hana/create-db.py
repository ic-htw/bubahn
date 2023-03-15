from hdbcli import dbapi
from hana_ml.dataframe import ConnectionContext

url = "61387a80-59c3-44a9-9bb5-f7738dcb1adf.hana.trial-us10.hanacloud.ondemand.com"

con = dbapi.connect(
    address="61387a80-59c3-44a9-9bb5-f7738dcb1adf.hana.trial-us10.hanacloud.ondemand.com",
    port=443,
    user="DBADMIN",
    password="Rkxy171+"
)


# cc = ConnectionContext(url, 443, "DBADMIN", "Rkxy171+")
# print(cc.hana_version())
# cc.close()

sql = """
--drop table halt;
--drop table fahrt;
--drop table zeitplan;
--drop table abschnitt;
--drop table segment;
--drop table unterlinie;
--drop table haltestelle;
--drop table linie;
"""
# con.execute(sql)

# -------------------------------------------------
# linie
# -------------------------------------------------
sql = """
create table linie (
    lid integer not null,
    bez varchar(10) not null,
    primary key (lid)
);

"""
with con.cursor() as cursor:
    cursor.execute(sql)


sql = """
insert into linie
  select * from read_csv_auto('../csv/linie.csv')
"""
# con.execute(sql)


# -------------------------------------------------
# haltestelle
# -------------------------------------------------
sql = """
create table haltestelle (
    hid integer not null,
    bez varchar(200) not null unique,
    lat float not null,
    lng float not null,
    primary key (hid)
);
"""
# con.execute(sql)

sql = """
insert into haltestelle
  select * from read_csv_auto('../csv/haltestelle.csv')
"""
# con.execute(sql)

# -------------------------------------------------
# unterlinie
# -------------------------------------------------
sql = """
create table unterlinie (
    ulid integer not null,
    lid integer not null,
    primary key (ulid)
);
"""
# con.execute(sql)

sql = """
insert into unterlinie
  select * from read_csv_auto('../csv/unterlinie.csv')
"""
# con.execute(sql)

# -------------------------------------------------
# segment
# -------------------------------------------------
sql = """
create table segment (
    hid_a integer not null,
    hid_b integer not null,
    laenge_in_meter integer,
    primary key (hid_a, hid_b)
);
"""
# con.execute(sql)

sql = """
insert into segment
  select * from read_csv_auto('../csv/segment.csv')
"""
# con.execute(sql)

# -------------------------------------------------
# abschnitt
# -------------------------------------------------
sql = """
create table abschnitt (
    ulid integer not null,
    nr integer not null,
    hid_a integer not null,
    hid_b integer not null,
    haelt char(1) not null,
    primary key (ulid, nr)
);
"""
# con.execute(sql)

sql = """
insert into abschnitt
  select * from read_csv_auto('../csv/abschnitt.csv')
"""
# con.execute(sql)

# -------------------------------------------------
# zeitplan
# -------------------------------------------------
sql = """
create table zeitplan (
    zpid integer not null,
    datum_beginn date not null,
    datum_ende date not null,
    mo integer not null,
    di integer not null,
    mi integer not null,
    "do" integer not null,
    fr integer not null,
    sa integer not null,
    so integer not null,
    primary key (zpid)
);
"""
# con.execute(sql)

sql = """
insert into zeitplan
  select * from read_csv_auto('../csv/zeitplan.csv')
"""
# con.execute(sql)

# -------------------------------------------------
# fahrt
# -------------------------------------------------
sql = """
create table fahrt (
    fid bigint not null,
    zpid integer not null,
    ulid integer not null,
    primary key (fid)
);
"""
# con.execute(sql)

sql = """
insert into fahrt
  select * from read_csv_auto('../csv/fahrt.csv')
"""
# con.execute(sql)

# -------------------------------------------------
# halt
# -------------------------------------------------
sql = """
create table halt (
    haid bigint not null,
    fid bigint not null,
    hid integer not null,
    nr integer not null,
    zeit_ankunft time,
    zeit_abfahrt time,
    primary key (haid)
);
"""
# con.execute(sql)

sql = """
insert into halt
  select * from read_csv_auto('../csv/halt.csv')
"""
# con.execute(sql)




print("ok")