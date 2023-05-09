select 
  l.bez,
  ul.ulid,
  ha.bez,
  hb.bez
from 
  linie l
  join unterlinie ul on ul.lid=l.lid
  join abschnitt a on a.ulid=ul.ulid
  join haltestelle ha on ha.hid=a.hid_a
  join haltestelle hb on hb.hid=a.hid_b
where ul.ulid in (1026002)
order by l.bez, ul.ulid, a.nr;

select
  l.bez,
  hs1.hid, hs1.bez, h1.nr, h1.zeit_ankunft, h1.zeit_abfahrt,
  f.fid,
  ul.ulid
from 
  fahrt f
  join halt h1 on h1.fid=f.fid
  join unterlinie ul on ul.ulid=f.ulid
  join linie l on ul.lid=l.lid
  join haltestelle hs1 on hs1.hid=h1.hid
where f.fid in (1019002011)
order by h1.nr;

  


