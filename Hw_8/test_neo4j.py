import os
import pytest
import dotenv

from neo4j import GraphDatabase
from Hw_8.neo4j_functions import ne04j


def test_create_db():
    test_db = "test"
    query = "CREATE (n:TestNode {name: 'test'})"
    ne04j.create_new_db(query, db_name=test_db)
    result = ne04j.db_list
    assert test_db in result


def test_get():
    query = "MATCH (n) RETURN n LIMIT 1"
    result = ne04j.get(query)
    assert isinstance(result, list)


def test_put():
    query = "CREATE (p:Pharmacy {name: 'Pharmacy Test', address: 'Street Test'})"
    ne04j.put(query)
    result = ne04j.get("MATCH (p:Pharmacy {name: 'Pharmacy Test'}) RETURN p")
    assert len(result) == 1


def delete_test_db():
    test_db = "test"
    query = "MATCH (n:TestNode {name: 'test'}) DETACH DELETE n"
    ne04j.put(query)
    ne04j.delete_db(test_db)
    result = ne04j.db_list
    assert test_db not in result
