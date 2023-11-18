"""
User Service
This module contains the UserService class which manages user operations such as creating a user, authenticating a user, reading a user, and getting a user by username. It also contains a function to list templates for a user. The UserService class uses a MongoDB instance to perform database operations.
"""
# type: ignore

# pylint: disable=W0212
from bson.objectid import ObjectId

from api.v1.src.db.mongo_db import MongoDB
from api.v1.src.utils.handlers import handle_db_operations


class UserService:
    """
    Class to manage user operations.
    """

    def __init__(self, db: MongoDB):
        self.db = db
        # self.neo4j = neo4j

    @handle_db_operations
    def create_user(self, user_data: dict) -> str:
        """
        Create a user with the `user_data` object.
        An org with the name of the user should be created if an organization
        is not provided in registration.

        Args:
            user_data (dict): The user data to be inserted.

        Returns:
            str: The ID of the inserted user.
        """

        # Create an organization if "org_name" is not provided
        if "org_name" not in user_data:
            org_name = user_data.get("username")
            user_data.update({"org_name": org_name})
            org_id = self.db.create(document_data=user_data, collection_name=org_name)
        else:
            # Assuming orgs are pre-existing and org_name uniquely identifies them
            org_name = user_data["org_name"]
            existing_org = self.db.read(
                query={"org_name": org_name}, collection_name=org_name
            )
            org_id = existing_org.get("_id") if existing_org else None

        if not org_id:
            return "Organization not found"

        # Update user data with org_id
        user_data["org_id"] = org_id

        # Create the user
        insert_result = self.db.create(document_data=user_data, collection_name="users")

        return insert_result.get("result")

    @handle_db_operations
    def authenticate_user(self, username: str, password: str) -> dict:
        """
        Authenticate a user by username and password.

        Args:
            username (str): The username of the user to be authenticated.
            password (str): The password of the user to be authenticated.

        Returns:
            dict: The user data if authentication is successful, None otherwise.
        """

        # Query for user with matching username and password
        user_data = self.db.read(
            query={"username": username, "password": password}, collection_name="users"
        )

        # Check if user is found and return user data, else return None
        if user_data:
            return user_data.get("result")
        else:
            return None

    def list_templates(self, user_id):
        from api.v1.src.services.templates_service import TemplateService

        list_templates = TemplateService(self.db).list_templates(user_id).get("result")

        # Return the new_template
        return list_templates

    @handle_db_operations
    def read_user(self, user_id: str) -> dict:
        """
        Read a user with the `user_id` object.

        Args:
            user_id (str): The user id to be read.

        Returns:
            dict: The user data if found, None otherwise.
        """
        try:
            # Convert user_id to ObjectId
            object_id = ObjectId(user_id)
        except Exception:
            return None  # or handle invalid user_id format

        # Query the database for the user
        user_data = self.db.read(query={"_id": object_id}, collection_name="users").get(
            "result"
        )

        user_templates = self.list_templates(user_id)
        user_data["starred_templates"] = []
        for i in range(len(user_templates)):
            if user_templates[i]["stars"] is not None:
                user_data["starred_templates"].append(user_templates[i])
        return user_data

    @handle_db_operations
    def get_user_by_username(self, username: str, projection: dict = None):  # type: ignore
        """
        Get a user by username.

        Args:
            username (str): The username of the user to be returned.

        Returns:
            dict: The user data.
        """
        projection = projection or {}

        user = self.db.read(
            query={"username": username},
            collection_name="users",
            projection=projection,
        ).get("result")
        return user