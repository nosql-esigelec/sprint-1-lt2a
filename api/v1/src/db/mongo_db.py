"""
MongoDB database operations.

This module contains the database operations for the MongoDB database.

Classes:
    MongoDB: A class to manage the database operations.

"""

#import logging
from typing import Optional, List, Union
#import datetime
#from bson.objectid import ObjectId
#from pymongo import errors
from api.v1.src.utils.handlers import handle_db_operations


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
    def drop_collection(self,
                        collection_name: str
                        ) -> dict:
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
    def drop_database(self,
                      database_name: str
                      ) -> dict:
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
    def drop_index(self,
                   collection_name: str,
                   index_name: str
                   ) -> dict:
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
        self,
        collection_name: str,
        field: str,
        unique: bool = False
    ) -> dict:
        """
        Create an index on the `collection` for the `field`.

        Args:
            collection_name (str): The collection name.
            field (str): The field name.
            unique (bool, optional): The uniqueness of the index.

        Returns:
            str: The name of the index.
        """

        collection = self.db[collection_name]
        index_name = collection.create_index([(field, 1)], unique=unique)
        return index_name
    
    @handle_db_operations
    def create(self,
               document_data: dict,
               collection_name: str,
               many: bool = False
               ) -> Union[str, List[str]]:
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
        collection = self.db[collection_name]
        if many:
            insert_result = collection.insert_many(document_data)
            return [str(doc_id) for doc_id in insert_result.inserted_ids]
        else:
            insert_result = collection.insert_one(document_data)
            return str(insert_result.inserted_id)

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
        Read one or more document(s) from the specified collection based on the query.

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

        collection = self.db[collection_name]
        if many:
            cursor = collection.find(query, projection)
            if sort:
                cursor = cursor.sort(sort)
            if skip is not None:
                cursor = cursor.skip(skip)
            cursor = cursor.limit(limit)
            documents = list(cursor)
            return documents
        else:
            document = collection.find_one(query, projection)
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

        collection = self.db[collection_name]

        if update_type == "set":
            update_operation = {"$set": document_data}
        if update_type == "push":
            update_operation = {"$push": document_data}
        if update_type == "pull":
            update_operation = {"$pull": document_data}
        if update_type == "unset":
            update_operation = {"$unset": document_data}
        if update_type == "inc":
            update_operation = {"$inc": document_data}
        else:
            return {"success": False, "message": "Invalid update type"}

        result = collection.update_many(query, update_operation)
        documents_updated_count = result.modified_count
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

        collection = self.db[collection_name]
        if many:
            result = collection.delete_many(query)
        else:
            result = collection.delete_one(query)

        documents_deleted_count = result.deleted_count
        return documents_deleted_count
