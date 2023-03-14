from neo4j import GraphDatabase
import cred_neo4j as c

def exe1(driver, *qs):
    # pass
    exe(driver, *qs)
    
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

    # exe1(driver, q1, q2)  
    # exe2(driver, q3, q4)  


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

    # exe1(driver, q1, q2)  
    # exe2(driver, q3, q4)  


    # -------------------------------------------------
    # 02 Segment
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
    # 03 xxx
    # -------------------------------------------------
    print("13 IS_LOCATED_IN")
    q1 = f"""
    MATCH (x:Company)-[z:IS_LOCATED_IN]->(y:Country) DETACH DELETE z;
    """

    q2 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Company.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      MATCH (x:Company {{id: toInteger(r.id)}})
      MATCH (y:Country {{id: toInteger(r.LocationPlaceId)}})
      CREATE (x)-[:IS_LOCATED_IN]->(y)
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    # exe1(driver, q1)  
    # exe2(driver, q2)  


# -------------------------------------------------
print("ok")
# -------------------------------------------------
