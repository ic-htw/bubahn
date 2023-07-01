psql -h lubuicla2.f4.htw-berlin.de -d adbkt -U umobility

\copy linie from '/mnt/c/work/lv/uebungen/databases/mobility/csv/linie.csv' delimiter ',' csv header;

\copy haltestelle(hid, bez, lat, lng ) from '/mnt/c/work/lv/uebungen/databases/mobility/csv/haltestelle.csv' delimiter ',' csv header;

\copy unterlinie from '/mnt/c/work/lv/uebungen/databases/mobility/csv/unterlinie.csv' delimiter ',' csv header;

\copy segment(hid_a, hid_b) from '/mnt/c/work/lv/uebungen/databases/mobility/csv/segment.csv' delimiter ','csv header;

\copy abschnitt from '/mnt/c/work/lv/uebungen/databases/mobility/csv/abschnitt.csv' delimiter ',' csv header;

\copy zeitplan from '/mnt/c/work/lv/uebungen/databases/mobility/csv/zeitplan.csv' delimiter ',' csv header;

\copy fahrt from '/mnt/c/work/lv/uebungen/databases/mobility/csv/fahrt.csv' delimiter ',' csv header;

\copy halt from '/mnt/c/work/lv/uebungen/databases/mobility/csv/halt.csv' delimiter ',' csv header;

update haltestelle set pos = ST_SetSRID(ST_MakePoint(lng, lat), 4326);
update haltestelle set posp = ST_Transform(pos, 31468);

update segment s set laenge_in_meter = ST_Distance(h1.pos::geography, h2.pos::geography) 
  from haltestelle h1, haltestelle h2 where h1.hid=s.hid_a and h2.hid=s.hid_b;

drop table segment_bi;
create table segment_bi as 
select hid_a, hid_b, laenge_in_meter from segment
union
select hid_b, hid_a, laenge_in_meter from segment;
