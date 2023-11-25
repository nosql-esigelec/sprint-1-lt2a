# pylint: ignore=invalid-name broad-except
"""
This module contains functions to connect to databases.

Functions:
- get_neo4j_db(): Creates a connection to a Neo4j database.
- get_mongo_db(database_name="gocod"): Returns a MongoDB database instance.
"""

import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

from api.v1.src.db.mongo_db import MongoDB
from api.v1.src.db.neo4j_db import Neo4jDB

dotenv_path = os.path.join(os.path.dirname(__file__), "..", "..", ".env")

load_dotenv(dotenv_path=dotenv_path)

mongo_uri = os.getenv(
    "MONGO_URI",
    "mongodb://mongo:password@34.76.255.124:27017/?retryWrites=true&w=majority",
)
uri = os.getenv("URI", "mongodb://mongo:password@34.76.255.124:27017/?retryWrites=true&w=majority")
user = os.getenv("USER", "mongo")
password = os.getenv("PASSWORD", "password")

neo4j_uri = os.getenv("NEO4J_URI", "bolt://35.205.122.100:7687")
neo4j_user = os.getenv("NEO4J_USERNAME", "neo4j")
neo4j_password = os.getenv("NEO4J_PASSWORD", "password")


def get_neo4j_db():
    """
    Get the Neo4j database connection.

    Returns:
        Neo4jDB: The Neo4j database connection object.
    """
    db = Neo4jDB(neo4j_uri, neo4j_user, neo4j_password)
    return db


def get_mongo_db(database_name="gocod"):
    """
    Returns a MongoDB database instance.

    Args:
        database_name (str): The name of the database to connect to. Defaults to "gocod".

    Returns:
        pymongo.database.Database: The MongoDB database instance.
    """
    client = MongoClient(mongo_uri, server_api=ServerApi("1"))
    try:
        client.admin.command("ping")
    except Exception as e:
        print(e)
    db = client[database_name]

    return MongoDB(db)
