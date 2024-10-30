import os

import dotenv
from neo4j import GraphDatabase, basic_auth, Session, Result
from neo4j._sync import driver

dotenv.load_dotenv()


class Neo4jCustom:
    current_database: str = "neo4j"

    def __init__(self, uri: str, user: str, password: str):
        """
        Initialize the connection

        :param uri: URL of the database
        :param user: Username to connect
        :param password: Password to connect
        """

        self._driver: driver = GraphDatabase.driver(uri, auth=basic_auth(user, password))

    def close(self) -> None:
        """
        Close the connection

        :return:
        """

        self._driver.close()

    def get(self, cypher_query: str, params: dict | None = None) -> list:
        """
        Get the data from the database

        :param cypher_query: the query to run
        :param params: custom parameters
        :return:
        """
        with self._driver.session(database=self.current_database) as session:
            response = session.read_transaction(
                lambda tx: tx.run(cypher_query, params).data())
            return response

    def put(self, cypher_query: str, params: dict | None = None) -> None:
        """
        Put the data into the database

        :param cypher_query: the query to run
        :param params: custom parameters
        :return:
        """

        with self._driver.session(database=self.current_database) as session:
            response = session.write_transaction(
                lambda tx: tx.run(cypher_query, params))
            return response

    def run(self, cypher_query: str, params: dict | None = None) -> Result:
        """
        Run the custom query

        :param cypher_query: the query to run
        :param params: custom parameters
        :return:
        """

        with self._driver.session(database=self.current_database) as session:
            response = session.run(cypher_query, params)
            return response

    def create_new_db(self, query: str, db_name: str = "NoSQLLNU") -> None:
        """
        Create a new database

        :param query: the query to run
        :param db_name: the name of the database
        :return:
        """
        session: Session

        with self._driver.session() as session:
            session.run(f'CREATE DATABASE {db_name}')

        self.current_database = db_name

        with self._driver.session(database=db_name) as session:
            response = session.run(query)
            return response

    @property
    def db_list(self) -> list:
        """
        Get the list of databases

        :return:
        """

        with self._driver.session(database="system") as session:
            response = session.run("SHOW DATABASES")
            return [res["name"] for res in response]


ne04j = Neo4jCustom(os.getenv("NEO4J_URI"), os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
