drop table halt;
drop table fahrt;
drop table zeitplan;
drop table abschnitt;
drop table segment;
drop table unterlinie;
drop table haltestelle;
drop table linie;


create table linie (
    lid integer not null,
    bez nvarchar(10) not null,
    primary key (lid)
);

create table haltestelle (
    hid integer not null,
    bez nvarchar(200) not null unique,
    lat double not null,
    lng double not null,
    pos st_point(4326) validation full,
    posp st_point(1000004326) validation full,
    primary key (hid)
);

create table unterlinie (
    ulid integer not null,
    lid integer not null,
    primary key (ulid)
);

create table segment (
    hid_a integer not null,
    hid_b integer not null,
    laenge_in_meter integer,
    primary key (hid_a, hid_b)
);


create table abschnitt (
    ulid integer not null,
    nr integer not null,
    hid_a integer not null,
    hid_b integer not null,
    haelt char(1) not null,
    primary key (ulid, nr)
);

create table zeitplan (
    zpid integer not null,
    datum_beginn date not null,
    datum_ende date not null,
    mo integer not null,
    di integer not null,
    mi integer not null,
    do integer not null,
    fr integer not null,
    sa integer not null,
    so integer not null,
    primary key (zpid)
);


create table fahrt (
    fid bigint not null,
    zpid integer not null,
    ulid integer not null,
    primary key (fid)
);

create table halt (
    haid bigint not null,
    fid bigint not null,
    hid integer not null,
    nr integer not null,
    zeit_ankunft time,
    zeit_abfahrt time,
    primary key (haid)
);


alter table unterlinie
  add foreign key (lid) references linie;

alter table segment
  add foreign key (hid_a) references haltestelle;
alter table segment
  add foreign key (hid_b) references haltestelle;

alter table abschnitt
  add foreign key (ulid) references unterlinie;
alter table abschnitt
  add foreign key (hid_a) references haltestelle;
alter table abschnitt
  add foreign key (hid_b) references haltestelle;

alter table fahrt
  add foreign key (zpid) references zeitplan;

alter table halt
  add foreign key (fid) references fahrt;
alter table halt
  add foreign key (hid) references haltestelle;

