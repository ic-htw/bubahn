-- @block
drop property graph bubahn_graph;
create property graph bubahn_graph
    vertex tables (
        haltestelle
        key (hid)
        properties (hid, bez)
    )
    edge tables (
        segment
        key (hid_a, hid_b)
        source key (hid_a) references haltestelle(hid)
        destination key (hid_b) references haltestelle(hid)
        properties (laenge_in_meter)
    );

GRANT READ ANY PROPERTY GRAPH TO public;

-- @block
alter session set current_schema=ububahn;

-- @block
-- @label xxx
-- @label yyy
select * from graph_table (bubahn_graph
  match
  (h1 is haltestelle where h1.hid=10296) -[s is segment]->{1,10}(h2 is haltestelle)
  columns (h1.hid as hid1, h1.bez as bez1, h2.hid as hid2, h2.bez as bez2)
);

-- @block
select
