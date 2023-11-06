"""
MongoDB database operations.

This module contains the database operations for the MongoDB database.

Classes:
    MongoDB: A class to manage the database operations.

"""

import logging
from typing import Optional, List, Union
import datetime
from bson.objectid import ObjectId
from pymongo import errors
from src.utils.handlers import handle_db_operations


class MongoDB:
    """
    A class to manage the database operations.
    """

    def __init__(self, db):
        """
        Initialize the database.
        """
        self.db = db

    @handle_db_operations
    def drop_collection(self, collection_name: str) -> dict:
        """
        Drop a collection from the database.

        Args:
            collection_name (str): The name of the collection to be dropped.

        Returns:
            dict: A dictionary containing the operation's success status, message, and result.
        """

        drop_result = self.db[collection_name].drop()
        return drop_result
    
    @handle_db_operations
    def drop_database(self, database_name: str) -> dict:
        """
        Drop a database from the database.

        Args:
            database_name (str): The name of the database to be dropped.

        Returns:
            dict: A dictionary containing the operation's success status, message, and result.
        """

        drop_result = self.db.drop()
        return drop_result

    @handle_db_operations
    def drop_index(self, collection_name: str, index_name: str) -> dict:
        """
        Drop an index from the collection.

        Args:
            collection_name (str): The name of the collection.
            index_name (str): The name of the index.

        Returns:
            dict: A dictionary containing the operation's success status, message, and result.
        """

        drop_result = self.db[collection_name].drop_index(index_name)
        return drop_result

    @handle_db_operations
    def create_index(
        self, collection_name: str, field: str, unique: bool = False
    ) -> dict:
        """
        Create an index on the `collection` for the `field`.

        Args:
            collection_name (str): The collection name.
            field (str): The field name.

        Returns:
            str: The name of the index.
        """
        # TODO(mongo): Create Index
        # (fixme, mongo): Implement the method to create an index on the collection for the field.
        # Refer to MongoDB documentation: https://docs.mongodb.com/manual/indexes/
        index_name = "placeholder"
        return index_name
    
    @handle_db_operations
    def create(self, document_data: dict, collection_name: str, many: bool = False) -> Union[str, List[str]]:
        """
        Create a document in a collection in the database.
        Used for create_org, create_project

        Args:
            document_data (dict): The data to be inserted.
            collection_name (str): The name of the MongoDB collection to be inserted into.
            many (bool, optional): Whether to insert many documents. Defaults to False.

        Returns:
            Union[str, List[str]]: The inserted document's ID or list of IDs.
        """
        # TODO(mongo): Create Document(s)
        # (fixme, mongo): Implement the method to create a new document or many documents in the database.
        # Refer to MongoDB documentation: https://docs.mongodb.com/manual/tutorial/insert-documents/
        insert_result = "placeholder"
        return insert_result

    @handle_db_operations
    def read(
        self,
        query: dict,
        collection_name: str,
        many: bool = False,
        projection: Optional[dict] = None,
        sort: Optional[List[tuple]] = None,
        limit: int = 10,
        skip: Optional[int] = None,
    ) -> Union[dict, List[dict]]:
        """
        Read a document(s) from the specified collection based on the query.

        Args:
            query (dict): The query of the document to be retrieved.
            collection_name (str): The name of the MongoDB collection to be queried.
            many (bool, optional): Whether to return many documents. Defaults to False.
            projection (dict, optional): Fields to include in the result. Defaults to None.
            sort (List[tuple], optional): Sorting order. Defaults to None.
            limit (int, optional): Maximum number of records to return. Defaults to 10.
            skip (int, optional): Number of records to skip. Defaults to None.

        Returns:
            Union[dict, List[dict]]: The retrieved document(s).
        """
        # TODO(mongo): Read Document(s)
        # (fixme, mongo): Implement the method to read a document or many documents in the database.
        # Refer to MongoDB documentation: https://docs.mongodb.com/manual/tutorial/query-documents/
        
        document = {} or [{},{}] #placeholder
        return document

    @handle_db_operations
    def update(
        self,
        query: dict,
        document_data: dict,
        collection_name: str,
        update_type: str = "set",
    ) -> int:
        """
        Update a document in a given collection in the database.

        Args:
            query (dict): The query of the document to be updated.
            document_data (dict): The data to be updated.
            collection_name (str): The name of the collection to be updated.
            update_type (str): The type of update to be performed. Defaults to "set".

        Returns:
            int: The number of modified documents.
        """
        # TODO(mongo): Update Document(s)
        # (fixme, mongo): Implement the method to update a document or many documents in the database.
        # Refer to MongoDB documentation: https://docs.mongodb.com/manual/tutorial/update-documents/
        if update_type not in ["set", "push", "pull", "unset", "inc"]:
            return {"success": False, "message": "Invalid update type"}
        
        collection = self.db[collection_name]
        
        documents_updated_count = 0 #placeholder
        return documents_updated_count
    @handle_db_operations
    def delete(self, query: dict, collection_name: str, many: bool = False) -> int:
        """
        Delete document(s) from the given collection in the database.

        Args:
            query (dict): The query of the document to be deleted.
            collection_name (str): The name of the collection to be deleted.
            many (bool, optional): Whether to delete many documents. Defaults to False.

        Returns:
            int: The number of deleted documents.
        """
        # TODO(mongo): Delete Document(s) 
        # (fixme, mongo): Implement the method to delete a document or many documents in the database.
        # Refer to MongoDB documentation: https://docs.mongodb.com/manual/tutorial/remove-documents/
        documents_deleted_count = 0 #placeholder
        return documents_deleted_count
