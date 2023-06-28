drop PROPERTY GRAPH BUBAHN_GRAPH
CREATE PROPERTY GRAPH BUBAHN_GRAPH
    VERTEX TABLES (
        Haltestelle
        KEY (HID)
        PROPERTIES (HID, Bez)
    )
    EDGE TABLES (
        Segment
        KEY (HID_A, HID_B)
        SOURCE KEY (HID_A) REFERENCES Haltestelle(HID)
        DESTINATION KEY (HID_B) REFERENCES Haltestelle(HID)
        PROPERTIES (Laenge_In_Meter)
    );


SELECT * FROM GRAPH_TABLE (BUBAHN_GRAPH
  MATCH
  (h1 IS Haltestelle WHERE h1.hid=10296) -[s IS Segment]->{1,10}(h2 IS Haltestelle)
  COLUMNS (h1.hid AS hid1, h1.bez AS bez1, h2.hid AS hid2, h2.bez AS bez2)
);