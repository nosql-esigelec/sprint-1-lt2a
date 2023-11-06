"""
Templates Service
"""
# pylint: disable=W0212
from ast import parse
from curses import meta
import logging
import json

from requests import get

from pymongo import errors

from bson.objectid import ObjectId
from src.utils.parsing import parse_mongo_id
from src.utils.handlers import build_query_sort_project

from src.db.mongo_db import MongoDB
# from src.db.neo4j_db import Neo4jDB
from src.services.users_service import UserService
from src.utils.handlers import handle_db_operations


class TemplateService:
    """
    Class to manage template operations.
    """

    def __init__(self, 
                 mongo: MongoDB = None, 
                #  neo4j: Neo4jDB = None
                 ):
        self.mongo = mongo
        # self.neo4j = neo4j

    @handle_db_operations
    def create_template(self, template_data: dict):
        """
        Create a template with the `template_data` object.

        Args:
            template_data (dict): The template data to be inserted.

        Returns:
            str: The ID of the inserted template.
        """

        is_private = template_data["is_private"]
        # TODO(both): Create a new template
        # Implement the method to create a new template.
        # Given the `is_private` flag, insert the template into the `templates` collection
        # or the `users` collection.
        if is_private:
            # (fixme, mongo) : When the template is private, it should be added to the
            # document of the user who created it.
            template_data['tid'] = template_data["template_name"]
            self.mongo.update(
                query={"_id": ObjectId(template_data["created_by"])},
                document_data={"templates": template_data},
                collection_name="users",
                update_type="push",
            ).get("result")
            result = {
                "key": "template_name",
                "value": template_data["template_name"],
            }

        else:
            # (fixme, mongo): When the template is public, it should be added to the
            # `templates` collection.
            insert_result = self.mongo.create(
                document_data=template_data,
                collection_name="templates"
            ).get("result")
            result = {
                "key": "_id", 
                "value": insert_result
                }
            template_data = parse_mongo_id(template_data, "template", True)

        # (fixme, neo4j): Create a new template in Neo4j
        # You can use the `create` method of the `self.neo4j` instance to create a template.
        # The `identifier` argument should be set to `tid`
        return result

    @handle_db_operations
    def read_template(self, template_id, user_id=None, read_by="template_name") -> dict:
        """
        Read a template from the `templates` collection or the `users` collection.

        Args:
            template_id (str): The ID of the template to be retrieved.
            user_id (str): The ID of the user to be retrieved.

        Returns:
            dict: The template data.
        """
        # TODO(mongo): Read template
        # Read template from the `templates` collection or the `users` collection.
        # You can use the `read` method of the `self.mongo` instance to read a template
        template = None
        if user_id:
            # (fixme, mongo): Read Template if user_id is provided
            # If the user_id is provided, read the template from the `users` collection.
            pass
        else:
            pass
            # (fixme, mongo): Read Template if user_id is not provided
            # If the user_id is not provided, read the template from the `templates` collection.

        return template

    @handle_db_operations
    def list_templates(self, user_id=None, page=0, templates_per_page=0) -> dict:
        """
        List templates from the `templates` collection or the `users` collection.

        Args:
            user_id (str): The ID of the user to be retrieved.

        Returns:
            dict: The template data.
        """
        # TODO(mongo): List Templates 
        # Implement the method is used to list and display in the UI.
        
        user_service = UserService(self.mongo)
        templates = [] #placeholder
        if user_id:
            # (fixme, mongo): List Templates if user_id is provided
            # You can use the `read_user` method of the `user_service` instance to read a user.
            pass
        else:
            pass
            # (fixme, mongo) List Templates if user_id is not provided
            # You can use the `get_templates` method of the `self` instance to get templates.

        return templates

    @handle_db_operations
    def delete_template(self, template_id, user_id=None):
        """
        Delete a template from the `templates` collection or the `users` collection.

        Args:
            template_id (str): The ID of the template to be retrieved.
            user_id (str): The ID of the user to be retrieved.

        Returns:
            str: The ID of the deleted template.
        """
        # TODO(both): Delete Template
        # Implement the method to delete a template either from the `templates` collection
        # or the `users` collection.
        if user_id:
            # (fixme, mongo): Delete Template if user_id is provided
            # You can use the `update` method to `pull` the specified template from the user
            # document corresponding to the `user_id` provided.
           delete_result = self.mongo.update(
                query={
                    "_id": ObjectId(user_id),
                },
                document_data={"templates": {"template_name": template_id}},
                collection_name="users",
                update_type="pull",
            ).get("result")
        else:
            delete_result = self.mongo.delete(
                query={"_id": ObjectId(template_id)}, collection_name="templates"
            ).get("result")
        
        #(fixme, neo4j): Delete Template from Neo4j
        # You can use the `delete` method of the `self.neo4j` instance to delete a template.
        return delete_result

    @handle_db_operations
    def star_template(self, user_id, template_id):
        """
        Star a template from the `templates` collection or the `users` collection.

        Args:
            user_id (str): The ID of the user to be retrieved.
            template_id (str): The ID of the template to be retrieved.

        Returns:
            dict: The template data.
        """
        # TODO(mongo): Star Template
        # You can use the `update` method to :
        # 1. `push` the specified template to the `starred_templates` array of the user
        # document corresponding to the `user_id` provided.
        # 2. `inc` the `stars` field of the template document corresponding to the
        # `template_id` provided, depending on whether the template is private or public.
        # Note: The template_id will be the template_name if the template is private.
        template = self.read_template(template_id, user_id=user_id).get("result")[
            "templates"
        ][0]
        # (fixme, mongo): Push the template to the `starred_templates` array of the user
        # document corresponding to the `user_id` provided.

        if template["is_private"]:
            # (fixme, mongo): Increment the `stars` field of the template document, under 
            # the `users` document corresponding to the `user_id` provided.
            self.mongo.update(

            ).get("result")
        else:
            # (fixme, mongo): Increment the `stars` field of the template document
            # in the `templates` collection
            self.mongo.update(

            ).get("result")

        template = self.read_template(template_id, user_id=user_id).get("result")[
            "templates"
        ][0]
        return template

    @handle_db_operations
    def share_template(self, template_id, user_id):
        """
        Share a template from the `users` collection to the `templates`(public) collection.

        Args:
            template_id (str): The ID of the template to be retrieved.
            user_id (str): The ID of the user to be retrieved.

        Returns:
            dict: The template data.
        """
        template = self.read_template(template_id, user_id=user_id).get("result")[
            "templates"
        ][0]
        template["is_private"] = False

        result = self.mongo.create(template, "templates").get("result")

        return result

    def get_templates(self, filters, page, templates_per_page):
        """
        Find templates from the `templates` collection.

        Args:
            filters (dict): The filters to be applied.
            page (int): The page number.
            templates_per_page (int): The number of templates per page.

        Returns:
            list: The template's data.
        """

        query, sort, project = build_query_sort_project(filters)
        if project:
            templates = self.mongo.db["templates"].find(query, project).sort(sort)
        else:
            templates = self.mongo.db["templates"].find(query).sort(sort)
        total_templates = 0
        if page == 0:
            total_templates = self.mongo.db["templates"].count_documents(query)
        templates = templates.skip(page * templates_per_page).limit(templates_per_page)

        return list(templates), total_templates
