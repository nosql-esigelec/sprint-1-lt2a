import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from db.mongo_db import MongoDB
# from src.db.neo4j_db import Neo4jDB

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')

load_dotenv(dotenv_path=dotenv_path)

mongo_uri = os.getenv("MONGO_URI")
uri = os.getenv("URI", None)
user = os.getenv("USER", None)
password = os.getenv("PASSWORD", None)

def get_neo4j_db():
    # TODO(neo4j): Create Neo4j database connection.
    # You can use the Neo4jDB class for this task.
    # Refer to Neo4j documentation: https://neo4j.com/docs/driver-manual/current/client-applications/
    pass


from pymongo import MongoClient, ServerApi

