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
    print("01 TagClass")
    q1 = f"""
    DROP CONSTRAINT c_tagclass;
    """
    
    q2 = f"""
    MATCH (x:TagClass) DETACH DELETE x;
    """

    q3 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/TagClass.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      CREATE (x:TagClass {{
        id: toInteger(r.id), 
        name: r.name
        }})
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    q4 = f"""
    CREATE CONSTRAINT c_tagclass FOR (x:TagClass) REQUIRE x.id IS UNIQUE;
    """

    exe1(driver, q1, q2)  
    exe2(driver, q3, q4)  

    # -------------------------------------------------
    # 02 Tag
    # -------------------------------------------------
    print("02 Tag")
    q1 = f"""
    DROP CONSTRAINT c_tag;
    """
    q2 = f"""
    MATCH (x:Tag) DETACH DELETE x;
    """

    q3 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Tag.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      CREATE (x:Tag {{
        id: toInteger(r.id), 
        name: r.name
        }})
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    q4 = f"""
    CREATE CONSTRAINT c_tag FOR (x:Tag) REQUIRE x.id IS UNIQUE;
    """

    exe1(driver, q1, q2)  
    exe2(driver, q3, q4)  
 
    # -------------------------------------------------
    # 03 Country
    # -------------------------------------------------
    print("03 Country")
    q1 = f"""
    DROP CONSTRAINT c_Country;
    """
    q2 = f"""
    MATCH (x:Country) DETACH DELETE x;
    """

    q3 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Country.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      CREATE (x:Country {{
        id: toInteger(r.id), 
        name: r.name
        }})
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    q4 = f"""
    CREATE CONSTRAINT c_Country FOR (x:Country) REQUIRE x.id IS UNIQUE;
    """

    exe1(driver, q1, q2)  
    exe2(driver, q3, q4)  

    # -------------------------------------------------
    # 04 City
    # -------------------------------------------------
    print("04 City")
    q1 = f"""
    DROP CONSTRAINT c_City;
    """
    q2 = f"""
    MATCH (x:City) DETACH DELETE x;
    """

    q3 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/City.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      CREATE (x:City {{
        id: toInteger(r.id), 
        name: r.name
        }})
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    q4 = f"""
    CREATE CONSTRAINT c_City FOR (x:City) REQUIRE x.id IS UNIQUE;
    """

    exe1(driver, q1, q2)  
    exe2(driver, q3, q4)  

    # -------------------------------------------------
    # 05 Company
    # -------------------------------------------------
    print("05 Company")
    q1 = f"""
    DROP CONSTRAINT c_Company;
    """
    q2 = f"""
    MATCH (x:Company) DETACH DELETE x;
    """

    q3 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Company.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      CREATE (x:Company {{
        id: toInteger(r.id), 
        name: r.name
        }})
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    q4 = f"""
    CREATE CONSTRAINT c_Company FOR (x:Company) REQUIRE x.id IS UNIQUE;
    """

    exe1(driver, q1, q2)  
    exe2(driver, q3, q4)  

    # -------------------------------------------------
    # 06 University
    # -------------------------------------------------
    print("06 University")
    q1 = f"""
    DROP CONSTRAINT c_University;
    """
    q2 = f"""
    MATCH (x:University) DETACH DELETE x;
    """

    q3 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/University.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      CREATE (x:University {{
        id: toInteger(r.id), 
        name:r.name
        }})
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    q4 = f"""
    CREATE CONSTRAINT c_University FOR (x:University) REQUIRE x.id IS UNIQUE;
    """

    exe1(driver, q1, q2)  
    exe2(driver, q3, q4)  

    # -------------------------------------------------
    # 07 Person
    # -------------------------------------------------
    print("07 Person")
    q1 = f"""
    DROP CONSTRAINT c_Person;
    """
    q2 = f"""
    MATCH (x:Person) DETACH DELETE x;
    """

    q3 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Person.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      CREATE (x:Person {{
        id: toInteger(r.id), 
        lastName: r.lastName, 
        creationDate: datetime(replace(r.creationDate, ' ', 'T'))
        }})
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    q4 = f"""
    CREATE CONSTRAINT c_Person FOR (x:Person) REQUIRE x.id IS UNIQUE;
    """

    exe1(driver, q1, q2)  
    exe2(driver, q3, q4)  
  

    # -------------------------------------------------
    # 08 Forum
    # -------------------------------------------------
    print("08 Forum")
    q1 = f"""
    DROP CONSTRAINT c_Forum;
    """
    q2 = f"""
    MATCH (x:Forum) DETACH DELETE x;
    """

    q3 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Forum.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      CREATE (x:Forum {{
        id: toInteger(r.id), 
        name: r.name, 
        creationDate: datetime(replace(r.creationDate, ' ', 'T'))
        }})
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    q4 = f"""
    CREATE CONSTRAINT c_Forum FOR (x:Forum) REQUIRE x.id IS UNIQUE;
    """

    exe1(driver, q1, q2)  
    exe2(driver, q3, q4)  

    # -------------------------------------------------
    # 09 Message
    # -------------------------------------------------
    print("09 Message")
    q1 = f"""
    DROP CONSTRAINT c_Message;
    """
    q2 = f"""
    call apoc.periodic.iterate(
      'MATCH (x:Message) return x', 
      'DETACH DELETE x', 
      {{batchSize:100000, batchMode:"BATCH"}}
    )
    """

    q3 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Message.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      CREATE (x:Message {{
        id: toInteger(r.id), 
        length: toInteger(r.length),
        ParentMessageId: toInteger(r.ParentMessageId), 
        creationDate: datetime(replace(r.creationDate, ' ', 'T'))
        }})
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    q4 = f"""
    CREATE CONSTRAINT c_Message FOR (x:Message) REQUIRE x.id IS UNIQUE;
    """

    exe1(driver, q1, q2)  
    exe2(driver, q3, q4)  

    # -------------------------------------------------
    # 09a Post
    # -------------------------------------------------
    print("09a Post")
    q1 = f"""
    DROP CONSTRAINT c_Post;
    """
    q2 = f"""
    MATCH (x:Message) where x.ParentMessageId is null set x:Post;
    """
    q3 = f"""
    CREATE CONSTRAINT c_Post FOR (x:Post) REQUIRE x.id IS UNIQUE;
    """

    exe1(driver, q1)  
    exe2(driver, q2, q3)  

    # -------------------------------------------------
    # 09b Comment
    # -------------------------------------------------
    print("09b Comment")
    q1 = f"""
    DROP CONSTRAINT c_Comment;
    """
    q2 = f"""
    MATCH (x:Message) where x.ParentMessageId is not null set x:Comment;
    """
    q3 = f"""
    CREATE CONSTRAINT c_Comment FOR (x:Comment) REQUIRE x.id IS UNIQUE;
    """

    exe1(driver, q1)  
    exe2(driver, q2, q3)  


    # -------------------------------------------------
    # 10 IS_SUBCLASS_OF
    # -------------------------------------------------
    print("10 IS_SUBCLASS_OF")
    q1 = f"""
    MATCH (x:TagClass)-[z:IS_SUBCLASS_OF]->(y:TagClass) DETACH DELETE z;
    """

    q2 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/TagClass.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      MATCH (x:TagClass {{id: toInteger(r.id)}})
      MATCH (y:TagClass {{id: toInteger(r.SubclassOfTagClassId)}})
      CREATE (x)-[:IS_SUBCLASS_OF]->(y)
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    exe1(driver, q1)  
    exe2(driver, q2)  

    # -------------------------------------------------
    # 11 HAS_TYPE
    # -------------------------------------------------
    print("11 HAS_TYPE")
    q1 = f"""
    MATCH (x:Tag)-[z:HAS_TYPE]->(y:TagClass) DETACH DELETE z;
    """

    q2 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Tag.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      MATCH (x:Tag {{id: toInteger(r.id)}})
      MATCH (y:TagClass {{id: toInteger(r.TypeTagClassId)}})
      CREATE (x)-[:HAS_TYPE]->(y)
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    exe1(driver, q1)  
    exe2(driver, q2)  

    # -------------------------------------------------
    # 12 IS_PART_OF
    # -------------------------------------------------
    print("12 IS_PART_OF")
    q1 = f"""
    MATCH (x:City)-[z:IS_PART_OF]->(y:Country) DETACH DELETE z;
    """

    q2 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/City.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      MATCH (x:City {{id: toInteger(r.id)}})
      MATCH (y:Country {{id: toInteger(r.PartOfCountryId)}})
      CREATE (x)-[:IS_PART_OF]->(y)
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    exe1(driver, q1)  
    exe2(driver, q2)  


    # -------------------------------------------------
    # 13 IS_LOCATED_IN
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

    exe1(driver, q1)  
    exe2(driver, q2)  


    # -------------------------------------------------
    # 14 IS_LOCATED_IN
    # -------------------------------------------------
    print("14 IS_LOCATED_IN")
    q1 = f"""
    MATCH (x:University)-[z:IS_LOCATED_IN]->(y:City) DETACH DELETE z;
    """

    q2 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/University.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      MATCH (x:University {{id: toInteger(r.id)}})
      MATCH (y:City {{id: toInteger(r.LocationPlaceId)}})
      CREATE (x)-[:IS_LOCATED_IN]->(y)
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    exe1(driver, q1)  
    exe2(driver, q2)  


    # -------------------------------------------------
    # 15 IS_LOCATED_IN
    # -------------------------------------------------
    print("15 IS_LOCATED_IN")
    q1 = f"""
    MATCH (x:Person)-[z:IS_LOCATED_IN]->(y:City) DETACH DELETE z;
    """

    q2 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Person.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      MATCH (x:Person {{id: toInteger(r.id)}})
      MATCH (y:City {{id: toInteger(r.LocationCityId)}})
      CREATE (x)-[:IS_LOCATED_IN]->(y)
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    exe1(driver, q1)  
    exe2(driver, q2)  


    # -------------------------------------------------
    # 16 IS_LOCATED_IN
    # -------------------------------------------------
    print("16 IS_LOCATED_IN")
    q1 = f"""
    MATCH (x:Message)-[z:IS_LOCATED_IN]->(y:Country) DETACH DELETE z;
    """

    q2 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Message.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      MATCH (x:Message {{id: toInteger(r.id)}})
      MATCH (y:Country {{id: toInteger(r.LocationCountryId)}})
      CREATE (x)-[:IS_LOCATED_IN]->(y)
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    exe1(driver, q1)  
    exe2(driver, q2)  


    # -------------------------------------------------
    # 17 STUDY_AT
    # -------------------------------------------------
    print("17 STUDY_AT")
    q1 = f"""
    MATCH (x:Person)-[z:STUDY_AT]->(y:University) DETACH DELETE z;
    """

    q2 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Person_studyAt_University.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      MATCH (x:Person {{id: toInteger(r.PersonId)}})
      MATCH (y:University {{id: toInteger(r.UniversityId)}})
      CREATE (x)-[:STUDY_AT {{creationDate: datetime(replace(r.creationDate, ' ', 'T'))}}]->(y)
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    exe1(driver, q1)  
    exe2(driver, q2)  


    # -------------------------------------------------
    # 18 WORK_AT
    # -------------------------------------------------
    print("18 WORK_AT")
    q1 = f"""
    MATCH (x:Person)-[z:WORK_AT]->(y:Company) DETACH DELETE z;
    """

    q2 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Person_workAt_Company.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      MATCH (x:Person {{id: toInteger(r.PersonId)}})
      MATCH (y:Company {{id: toInteger(r.CompanyId)}})
      CREATE (x)-[:WORK_AT {{creationDate: datetime(replace(r.creationDate, ' ', 'T'))}}]->(y)
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    exe1(driver, q1)  
    exe2(driver, q2)  


    # -------------------------------------------------
    # 19 KNOWS
    # -------------------------------------------------
    print("19 KNOWS")
    q1 = f"""
    MATCH (x:Person)-[z:KNOWS]->(y:Person) DETACH DELETE z;
    """

    q2 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Person_knows_Person.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      MATCH (x:Person {{id: toInteger(r.Person1Id)}})
      MATCH (y:Person {{id: toInteger(r.Person2Id)}})
      CREATE (x)-[:KNOWS {{creationDate: datetime(replace(r.creationDate, ' ', 'T'))}}]->(y)
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    exe1(driver, q1)  
    exe2(driver, q2)  


    # -------------------------------------------------
    # 20 HAS_INTEREST
    # -------------------------------------------------
    print("20 HAS_INTEREST")
    q1 = f"""
    MATCH (x:Person)-[z:HAS_INTEREST]->(y:Tag) DETACH DELETE z;
    """

    q2 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Person_hasInterest_Tag.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      MATCH (x:Person {{id: toInteger(r.PersonId)}})
      MATCH (y:Tag {{id: toInteger(r.TagId)}})
      CREATE (x)-[:HAS_INTEREST {{creationDate: datetime(replace(r.creationDate, ' ', 'T'))}}]->(y)
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    exe1(driver, q1)  
    exe2(driver, q2)  

    # -------------------------------------------------
    # 21 LIKES
    # -------------------------------------------------
    print("21 LIKES")
    q1 = f"""
    MATCH (x:Person)-[z:LIKES]->(y:Message) DETACH DELETE z;
    """

    q2 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Person_likes_Message.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      MATCH (x:Person {{id: toInteger(r.PersonId)}})
      MATCH (y:Message {{id: toInteger(r.id)}})
      CREATE (x)-[:LIKES {{creationDate: datetime(replace(r.creationDate, ' ', 'T'))}}]->(y)
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    exe1(driver, q1)  
    exe2(driver, q2)  



    # -------------------------------------------------
    # 22 HAS_MEMBER
    # -------------------------------------------------
    print("22 HAS_MEMBER")
    q1 = f"""
    MATCH (x:Forum)-[z:HAS_MEMBER]->(y:Person) DETACH DELETE z;
    """

    q2 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Forum_hasMember_Person.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      MATCH (x:Forum {{id: toInteger(r.ForumId)}})
      MATCH (y:Person {{id: toInteger(r.PersonId)}})
      CREATE (x)-[:HAS_MEMBER {{creationDate: datetime(replace(r.creationDate, ' ', 'T'))}}]->(y)
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    exe1(driver, q1)  
    exe2(driver, q2)  

    # -------------------------------------------------
    # 23 HAS_TAG
    # -------------------------------------------------
    print("23 HAS_TAG")
    q1 = f"""
    MATCH (x:Forum)-[z:HAS_TAG]->(y:Tag) DETACH DELETE z;
    """

    q2 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Forum_hasTag_Tag.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      MATCH (x:Forum {{id: toInteger(r.ForumId)}})
      MATCH (y:Tag {{id: toInteger(r.TagId)}})
      CREATE (x)-[:HAS_TAG {{creationDate: datetime(replace(r.creationDate, ' ', 'T'))}}]->(y)
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    exe1(driver, q1)  
    exe2(driver, q2)  

    # -------------------------------------------------
    # 24 HAS_MODERATOR
    # -------------------------------------------------
    print("24 HAS_MODERATOR")
    q1 = f"""
    MATCH (x:Forum)-[z:HAS_MODERATOR]->(y:Person) DETACH DELETE z;
    """

    q2 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Forum.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      MATCH (x:Forum {{id: toInteger(r.id)}})
      MATCH (y:Person {{id: toInteger(r.ModeratorPersonId)}})
      CREATE (x)-[:HAS_MODERATOR]->(y)
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    exe1(driver, q1)  
    exe2(driver, q2)  

    # -------------------------------------------------
    # 25 CONTAINER_OF
    # -------------------------------------------------
    print("25 CONTAINER_OF")
    q1 = f"""
    MATCH (x:Forum)-[z:CONTAINER_OF]->(y:Post) DETACH DELETE z;
    """

    q2 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Message.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      MATCH (x:Forum {{id: toInteger(r.ContainerForumId)}})
      MATCH (y:Post {{id: toInteger(r.id)}})
      CREATE (x)-[:CONTAINER_OF]->(y)
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    exe1(driver, q1)  
    exe2(driver, q2)  

    # -------------------------------------------------
    # 26 HAS_CREATOR
    # -------------------------------------------------
    print("26 HAS_CREATOR")
    q1 = f"""
    MATCH (x:Message)-[z:HAS_CREATOR]->(y:Person) DETACH DELETE z;
    """

    q2 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Message.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      MATCH (x:Message {{id: toInteger(r.id)}})
      MATCH (y:Person {{id: toInteger(r.CreatorPersonId)}})
      CREATE (x)-[:HAS_CREATOR]->(y)
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    exe1(driver, q1)  
    exe2(driver, q2)  

    # -------------------------------------------------
    # 27 HAS_TAG
    # -------------------------------------------------
    print("27 HAS_TAG")
    q1 = f"""
    MATCH (x:Message)-[z:HAS_TAG]->(y:Tag) DETACH DELETE z;
    """

    q2 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Message_hasTag_Tag.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      MATCH (x:Message {{id: toInteger(r.id)}})
      MATCH (y:Tag {{id: toInteger(r.TagId)}})
      CREATE (x)-[:HAS_TAG {{creationDate: datetime(replace(r.creationDate, ' ', 'T'))}}]->(y)
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    exe1(driver, q1)  
    exe2(driver, q2)  

    # -------------------------------------------------
    # 28 REPLY_OF
    # -------------------------------------------------
    print("28 REPLY_OF")
    q1 = f"""
    MATCH (x:Comment)-[z:REPLY_OF]->(y:Message) DETACH DELETE z;
    """

    q2 = f"""
    LOAD CSV WITH HEADERS FROM 'file:///sozmed/Message.csv' AS r FIELDTERMINATOR '|'
    CALL {{
      WITH r
      MATCH (x:Comment {{id: toInteger(r.id)}})
      MATCH (y:Message {{id: toInteger(r.ParentMessageId)}})
      CREATE (x)-[:REPLY_OF]->(y)
    }} IN TRANSACTIONS OF 100000 ROWS;
    """

    exe1(driver, q1)  
    exe2(driver, q2)  



# -------------------------------------------------
print("ok")
# -------------------------------------------------
