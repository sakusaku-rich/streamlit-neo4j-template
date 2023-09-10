import os
from functools import lru_cache
from neo4j import GraphDatabase, RoutingControl


@lru_cache(maxsize=1)
def neo4j(
    url: str = os.environ.get("NEO4J_URI"),
    username: str = os.environ.get("NEO4J_USERNAME"),
    password: str = os.environ.get("NEO4J_PASSWORD")
    ) -> object:
    driver = GraphDatabase.driver(
        url,
        auth=(username, password)
    )
    return driver

def example_match_persons():
    with neo4j() as n4j:
        records, _, _ = n4j.execute_query(
            """
            MATCH (n:Person)
            RETURN n.name as name
            LIMIT 10
            """,
            database_="neo4j", 
            routing_=RoutingControl.READ,
        )
        persons = [
            r["name"] for r in records
        ]
    return persons
        