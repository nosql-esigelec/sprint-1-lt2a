import os
from dotenv import load_dotenv

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from src.db.mongo_db import MongoDB
# from src.db.neo4j_db import Neo4jDB


load_dotenv()

mongo_uri = os.getenv(
    "MONGO_URI"
)
uri = os.getenv("URI", None)
user = os.getenv("USER", None)
password = os.getenv("PASSWORD", None)

def get_neo4j_db():
    # TODO(neo4j): Create Neo4j database connection.
    # You can use the Neo4jDB class for this task.
    # Refer to Neo4j documentation: https://neo4j.com/docs/driver-manual/current/client-applications/
    pass


def get_mongo_db(database_name="evops_db"):
    # TODO(mongo): Create a MongoDB connection 
    # that will be reused in the other methods.
    # You should use the MongoClient class and ServerApi for this task.
    # Don't forget to select the correct database.
    # Refer to MongoDB documentation: https://docs.mongodb.com/drivers/python/sync/current/fundamentals/connection/
    pass
