"""
User Service
"""
# pylint: disable=W0212
import logging
from bson.objectid import ObjectId
from pymongo import errors
from src.db.mongo_db import MongoDB
from src.utils.handlers import handle_db_operations


class UserService:
    """
    Class to manage user operations.
    """
    def __init__(self, db):
        self.db = db
    
    @handle_db_operations
    def create_user(self, user_data: dict):
        """
        Create a user with the `user_data` object.
        An org with the name of the user should be created if an organization
        is not provided in registration.

        Args:
            user_data (dict): The user data to be inserted.

        Returns:
            str: The ID of the inserted user.
        """
        # TODO(mongo): Create a new user.
        # If "org_name" is not in user_data, create an organization with the name of the user.
        # Create the user with the organization ID.
        # Refer to MongoDB documentation: https://docs.mongodb.com/manual/tutorial/insert-documents/
        if "org_name" not in user_data.keys():
            org_data = "placeholder"
        else:
            org_data = {"org_name": user_data["org_name"]}
 
        # org_id = self.db.create(org_data, "orgs").get("result")

        insert_result = "placeholder"
        return insert_result
    
    @handle_db_operations
    def authenticate_user(self, username: str, password: str):
        """
        Authenticate a user by username and password.

        Args:
            username (str): The username of the user to be authenticated.
            password (str): The password of the user to be authenticated.

        Returns:
            dict: The user data.
        """
        # TODO(mongo): Authenticate a user
        # Implement the method to authenticate a user by username and password.
        # You can use the `read` method of the MongoDB class to get a user by username and password.
        # Refer to MongoDB documentation: https://docs.mongodb.com/manual/tutorial/query-documents/
        pass
    
    @handle_db_operations
    def read_user(self, user_id: str):
        """
        Read a user with the `user_id` object.

        Args:
            user_id (str): The user id to be read.

        Returns:
            dict: The user data.
        """
        # TODO(mongo): Read user by their user ID.
        # Implement the method to read a user document given his user ID.
        pass

    @handle_db_operations
    def get_user_by_username(self, username: str, projection: dict = None):
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
