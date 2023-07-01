-- @block  
show search_path;

-- @block  
set search_path=umobility;

-- @block  
select * from segment;

-- @block  
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

-- @block  
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

-- @block  
with recursive paths(startnode, endnode, path) as (
   select
        hid_a as startnode,
        hid_b as endnode,
        array[hid_a, hid_b] as path
     from segment
     where startnode = 10152 -- Heidelberger Platz
   union all
   select 
        paths.startnode as startnode,
        hid_b as endnode,
        array_append(path, hid_b) as path
     from paths
     join edge on paths.endnode = hid_a
    where not hid_b=any(paths.path)
)
select startnode, endnode, path
from paths
order by length(path), path;

-- @block  
set search_path=umobility;

-- @block  
with recursive paths(startnode, endnode, path) as (
   select
        hid_a as startnode,
        hid_b as endnode,
        array[hid_a, hid_b] as path
     from segment
     where hid_a = 10152 -- Heidelberger Platz
   union all
   select 
        paths.startnode as startnode,
        hid_b as endnode,
        array_append(path, hid_b) as path
     from paths
     join segment on paths.endnode = hid_a
   where not hid_b=any(paths.path)
)
select startnode, endnode, path
from paths
order by  array_length(path, 1), path;