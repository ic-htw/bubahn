from neo4j import GraphDatabase
import cred_neo4j as c

def exe1(driver, *qs):
    pass
    # exe(driver, *qs)
    
def exe2(driver, *qs):
    # pass
    exe(driver, *qs)
    
def exe(driver, *qs):
    with driver.session() as session:
        for q in qs:
          session.run(q)

with GraphDatabase.driver(c.neo4j_host, auth=(c.neo4j_userid, c.neo4j_password)) as driver:

    # -------------------------------------------------
    # 01 TagClass
    # -------------------------------------------------
    print("01 Haltestelle")
    q1 = f"""
    DROP CONSTRAINT c_haltestelle;
    """
    
    q2 = f"""
    MATCH (x:Haltestelle) DETACH DELETE x;
    """

    q3 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///bubahn/haltestelle.csv' AS r FIELDTERMINATOR ','
    CALL {{
      WITH r
      CREATE (x:Haltestelle {{
        hid: toInteger(r.HID), 
        bez: r.BEZ
        }})
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    q4 = f"""
    CREATE CONSTRAINT c_haltestelle FOR (x:Haltestelle) REQUIRE x.id IS UNIQUE;
    """

    exe1(driver, q1, q2)  
    exe2(driver, q3, q4)  


    # -------------------------------------------------
    # 02 Linie
    # -------------------------------------------------
    print("02 Linie")
    q1 = f"""
    DROP CONSTRAINT c_linie;
    """
    
    q2 = f"""
    MATCH (x:Linie) DETACH DELETE x;
    """

    q3 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///bubahn/linie.csv' AS r FIELDTERMINATOR ','
    CALL {{
      WITH r
      CREATE (x:Linie {{
        lid: toInteger(r.LID), 
        bez: r.BEZ
        }})
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    q4 = f"""
    CREATE CONSTRAINT c_linie FOR (x:Linie) REQUIRE x.id IS UNIQUE;
    """

    exe1(driver, q1, q2)  
    exe2(driver, q3, q4)  


    # -------------------------------------------------
    # 03 Segment
    # -------------------------------------------------
    print("03 Segment")
    q2 = f"""
    MATCH (x:Segment) DETACH DELETE x;
    """

    q3 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///bubahn/segment.csv' AS r FIELDTERMINATOR ','
    CALL {{
      WITH r
      CREATE (x:Segment {{
        hid_a: toInteger(r.hid_a), 
        hid_b: toInteger(r.hid_b), 
        laenge_in_meter: toInteger(r.laenge_in_meter) 
        }})
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    exe1(driver, q2)  
    exe2(driver, q3)  


    # -------------------------------------------------
    # 04 Unterlinie
    # -------------------------------------------------
    print("04 Unterlinie")
    q1 = f"""
    DROP CONSTRAINT c_unterlinie;
    """
    
    q2 = f"""
    MATCH (x:Unterlinie) DETACH DELETE x;
    """

    q3 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///bubahn/unterlinie.csv' AS r FIELDTERMINATOR ','
    CALL {{
      WITH r
      CREATE (x:Unterlinie {{
        ulid: toInteger(r.ULID), 
        lid: toInteger(r.LID)
        }})
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    q4 = f"""
    CREATE CONSTRAINT c_unterlinie FOR (x:Unterlinie) REQUIRE x.id IS UNIQUE;
    """

    exe1(driver, q1, q2)  
    exe2(driver, q3, q4)  

    # -------------------------------------------------
    # 05 Abschnitt
    # -------------------------------------------------
    print("05 Abschnitt")
    q2 = f"""
    MATCH (x:Abschnitt) DETACH DELETE x;
    """

    q3 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///bubahn/abschnitt.csv' AS r FIELDTERMINATOR ','
    CALL {{
      WITH r
      CREATE (x:Abschnitt {{
        ulid: toInteger(r.ULID), 
        nr: toInteger(r.NR), 
        hid_a: toInteger(r.HID_A), 
        hid_b: toInteger(r.HID_B), 
        haelt: r.HAELT
        }})
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    exe1(driver, q2)  
    exe2(driver, q3)  


    # -------------------------------------------------
    # 06 ProjSegA
    # -------------------------------------------------
    print("06 ProjSegA")
    q1 = f"""
    MATCH (x:Segment)-[z:ProjSegA]->(y:Haltestelle) DETACH DELETE z;
    """

    q2 = f"""
    MATCH (x:Segment)
    WITH x, x.hid_a as hid_a, x.hid_b as hid_b
    MATCH (y:Haltestelle {{hid: hid_a}})
    CREATE (x)-[:ProjSegA]->(y)
    """

    exe1(driver, q1)  
    exe2(driver, q2)  


    # -------------------------------------------------
    # 07 ProjSegB
    # -------------------------------------------------
    print("07 ProjSegB")
    q1 = f"""
    MATCH (x:Segment)-[z:ProjSegB]->(y:Haltestelle) DETACH DELETE z;
    """

    q2 = f"""
    MATCH (x:Segment)
    WITH x, x.hid_a as hid_a, x.hid_b as hid_b
    MATCH (y:Haltestelle {{hid: hid_b}})
    CREATE (x)-[:ProjSegB]->(y)
    """

    exe1(driver, q1)  
    exe2(driver, q2)  


    # -------------------------------------------------
    # 08 InL
    # -------------------------------------------------
    print("08 InL")
    q1 = f"""
    MATCH (x:Unterlinie)-[z:InL]->(y:Linie) DETACH DELETE z;
    """

    q2 = f"""
    MATCH (x:Unterlinie)
    WITH x, x.lid as lid
    MATCH (y:Linie {{lid: lid}})
    CREATE (x)-[:InL]->(y)
    """

    exe1(driver, q1)  
    exe2(driver, q2)  


    # -------------------------------------------------
    # 09 InUL
    # -------------------------------------------------
    print("09 InUL")
    q1 = f"""
    MATCH (x:Abschnitt)-[z:InUL]->(y:Unterlinie) DETACH DELETE z;
    """

    q2 = f"""
    MATCH (x:Abschnitt)
    WITH x, x.ulid as ulid
    MATCH (y:Unterlinie {{ulid: ulid}})
    CREATE (x)-[:InUL]->(y)
    """

    exe1(driver, q1)  
    exe2(driver, q2)  


    # -------------------------------------------------
    # 10 ProjAbA
    # -------------------------------------------------
    print("10 ProjAbA")
    q1 = f"""
    MATCH (x:Abschnitt)-[z:ProjAbA]->(y:Haltestelle) DETACH DELETE z;
    """

    q2 = f"""
    MATCH (x:Abschnitt)
    WITH x, x.hid_a as hid_a, x.hid_b as hid_b
    MATCH (y:Haltestelle {{hid: hid_a}})
    CREATE (x)-[:ProjAbA]->(y)
    """

    exe1(driver, q1)  
    exe2(driver, q2)  


    # -------------------------------------------------
    # 11 ProjAbB
    # -------------------------------------------------
    print("11 ProjAbA")
    q1 = f"""
    MATCH (x:Abschnitt)-[z:ProjAbB]->(y:Haltestelle) DETACH DELETE z;
    """

    q2 = f"""
    MATCH (x:Abschnitt)
    WITH x, x.hid_a as hid_a, x.hid_b as hid_b
    MATCH (y:Haltestelle {{hid: hid_b}})
    CREATE (x)-[:ProjAbB]->(y)
    """

    exe1(driver, q1)  
    exe2(driver, q2)  


# -------------------------------------------------
print("ok")
# -------------------------------------------------
