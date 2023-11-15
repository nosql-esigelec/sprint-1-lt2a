# type: ignore
"""
Templates Service
"""
# pylint: disable=W0212
from ast import parse
from curses import meta #type: ignore 
import logging
import json
import uuid
from requests import get #type: ignore 

from pymongo import errors
from typing import Optional
from bson.objectid import ObjectId
from api.v1.src.utils.parsing import parse_mongo_id
from api.v1.src.utils.handlers import build_query_sort_project, generate_response

from api.v1.src.db.mongo_db import MongoDB
# from src.db.neo4j_db import Neo4jDB
from api.v1.src.services.users_service import UserService
from api.v1.src.utils.handlers import handle_db_operations


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

        is_private = template_data.get("is_private", False)

        if self.mongo is not None:
            if is_private:
                # Generate a uuid for that template
                template_uuid = uuid.uuid4().hex
                
                # Add the uuid to the template data
                template_data["template_id"] = template_uuid
                template_data["stars"] = 0
                
                # Add template to the user's document in the 'users' collection
                update_result = self.mongo.update(
                    query={"_id": ObjectId(template_data["created_by"])},
                    document_data=template_data,
                    update_type="push",
                    collection_name="users"
                ).get("result")
                result = {
                    'name': {
                        'template_name': template_data["template_name"]
                    },
                    'id': {
                        'template_id': template_uuid
                    }
                }
            else:
                # Add template to the 'templates' collection
                template_data["stars"] = 0
                insert_result = self.mongo.create(
                    #query={"created_by": template_data["created_by"]},
                    document_data=template_data,
                    #update_type="push",
                    collection_name="templates"
                ).get("result")
                result = {
                    "key": "_id", 
                    "value": insert_result
                    }
                template_data = parse_mongo_id(template_data, "template", True)
            # TODO: Create a new template in Neo4j
            # Example: self.neo4j.create(identifier=template_data.get('tid', ''), data=template_data)
            # Add your Neo4j creation logic here

            return result
        else: 
            message = f"MongoDB instance is not set."
            return message  


    @handle_db_operations
    def read_template(self, template_id, user_id=None, read_by="template_name") -> dict:
        if self.mongo is None:
            return {"MongoDB instance is not set."}
        template = []
        templates = []
        #try:
        if user_id:
            # Reading a private template
            user_object_id = ObjectId(user_id)
            user_data = self.mongo.read(query={"_id": user_object_id,
                                            "template_id": template_id
                                            }, 
                                        collection_name="users").get("result")
            if user_data and user_data['is_private'] == []:
                template = "ici"
            elif user_data and "template_name" in user_data:
                templates = [{
                    '_id': user_data['_id'],
                    'created_by': user_data['created_by'],
                    'is_private': user_data['is_private'],
                    'template_name': user_data['template_name'],
                    'template_id': user_data['template_id'],
                    'stars': user_data['stars'] if 'stars' in user_data else 0
                } for i in range(len(user_data['created_by']))
                        ]
                # Select the template which id matches 
                for a_template in templates:
                    if a_template["template_id"] == template_id and a_template['is_private'] == True:
                        template = a_template
                    else:
                        template = None
            else:
                template = None
        else:
            # Reading a public template
            template_object_id = ObjectId(template_id)
            user_data = self.mongo.read(query={"_id": ObjectId(template_object_id)}, collection_name="templates").get("result")
            if user_data and "template_name" in user_data:
                templates = [{
                    '_id': user_data['_id'],
                    'created_by': user_data['created_by'],
                    'is_private': user_data['is_private'],
                    'template_name': user_data['template_name'],
                    'stars': user_data['stars'] if 'stars' in user_data else 0
                } for i in range(len(user_data['created_by']))
                        ]
                # Select the template which id matches 
                for a_template in templates:
                    if a_template["_id"] == template_id:
                        template = a_template
            else:
                template = user_data
                
        if template:
            return template
        else:
            user_data = self.mongo.read(query={"created_by": user_id}, collection_name="templates").get("result")
            if user_data and "template_name" in user_data:
                templates = [{
                    '_id': user_data['_id'],
                    'created_by': user_data['created_by'],
                    'is_private': user_data['is_private'],
                    'template_name': user_data['template_name'],
                    'stars': user_data['stars'] if 'stars' in user_data else 0
                } for i in range(len(user_data['created_by']))
                        ]
                # Select the template which id matches 
                for a_template in templates:
                    if a_template["_id"] == template_id:
                        template = a_template
            else:
                template = templates
            if template == []:
                template = None
            return template[0] if template else template
        
        """except Exception as e:
            return {e}"""

    @handle_db_operations
    def list_templates(self, user_id=None, page=0, templates_per_page=10) -> list:
        """
        List templates from the `templates` collection or the `users` collection.

        Args:
            user_id (str, optional): The ID of the user to list templates for.
            page (int, optional): The page number for pagination. Defaults to 0.
            templates_per_page (int, optional): The number of templates per page for pagination. Defaults to 10.

        Returns:
            list: A List of template data.
        """
        if user_id:
            # List private templates for a specific user
            try:
                user_object_id = ObjectId(user_id)  # Make sure to convert to ObjectId
            except Exception:
                return {"Invalid user ID format"}

            user_data = self.mongo.read( 
                query={"_id": user_object_id},
                collection_name="users"
            ).get("result")
            
            if user_data is not None and "created_by" in user_data.keys(): 
                list_templates = [
                    {
                        'created_by': user_data['created_by'][i],
                        'is_private': user_data['is_private'][i],
                        'template_name': user_data['template_name'][i],
                        'template_id': user_data['template_id'][i],
                        'stars': user_data['stars'][i] if 'stars' in user_data else 0
                    } for i in range(len(user_data['created_by']))
                ]
                return list_templates
            else: 
                user_data = self.mongo.read( 
                    query= {"created_by": user_id},
                    collection_name="templates",
                    many=True
                ).get("result")
                if user_data is not None:
                    return user_data
                else:
                    return ["No templates found for this user"]
        else:
            # List public templates
            templates = self.mongo.read( 
                query={},
                collection_name="templates",
                many=True,
                limit=templates_per_page,
                skip=page * templates_per_page
            ).get("result")
            return templates

        return []

    @handle_db_operations
    def delete_template(self, template_id, user_id=None):
        """
        Delete a template from the `templates` collection or the `users` collection.

        Args:
            template_id (str): The ID of the template to be deleted.
            user_id (str, optional): The ID of the user whose template is to be deleted.

        Returns:
            str: The ID of the deleted template.
        """
        if user_id:
            # Delete a private template from the user's document in the 'users' collection
            user_object_id = ObjectId(user_id)
            """
            delete_count = self.mongo.delete(
                query={"_id": user_object_id,
                        "template_id": template_id},
                collection_name="users"
            ).get("result")
            delete_result = template_id if delete_count > 0 else None"""
            user_data = self.mongo.read(
                query={"_id": ObjectId(user_id),
                        "template_id": template_id},
                collection_name="users"
            ).get("result")
            for i in user_data["template_id"]:
                if i == template_id:
                    index = user_data["template_id"].index(i)
                    user_data["template_id"].pop(index)
                    user_data["template_name"].pop(index)
                    user_data["is_private"].pop(index)
                    user_data["stars"].pop(index)
                    break
            delete_result = self.mongo.update(
                query={"_id": ObjectId(user_id)},
                document_data=user_data,
                update_type="set",
                collection_name="users"
            ).get("result")
            delete_result = template_id
        else:
            # Delete a public template from the 'templates' collection
            delete_count = self.mongo.delete(
                query={"_id": ObjectId(template_id)},
                collection_name="templates"
            ).get("result")
            delete_result = template_id 

        # TODO: Delete Template from Neo4j
        # Example: self.neo4j.delete(template_id)
        # Add your Neo4j deletion logic here

        return delete_result if delete_result else -1

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
        template = self.read_template(template_id, user_id=user_id).get("result")
        if not template:
            return "nothing" # or raise an exception
        """
        # Push the template to the `starred_templates` array of the user document
        self.mongo.update(
            query={"_id": ObjectId(user_id)},
            document_data={"$push": {"starred_templates": template_id}},
            collection_name="users"
        )"""

        # Check if the template is private and update stars accordingly
        if template.get("is_private"):
            # Increment the `stars` field of the private template document under the user document
            #tid = template.get("template_id")
            user_data = self.mongo.read(
                query={"_id": ObjectId(user_id),
                        "template_id": template_id},
                collection_name="users"
            ).get("result")
            """
            list_templates = [
                    {
                        'created_by': user_data['created_by'][i],
                        'is_private': user_data['is_private'][i],
                        'template_name': user_data['template_name'][i],
                        'template_id': user_data['template_id'][i],
                        'stars': user_data['stars'][i] if 'stars' in user_data else 0
                    } for i in range(len(user_data['created_by']))
                ]
            for i in range(len(list_templates)):
                if list_templates[i]['template_id'] == template_id:
                    list_templates[i]['stars'] += 1
                    target_template = list_templates[i]
                    break
            #self.mongo.delete({"template_id":template_id, "template_name":target_template["template_name"]}, "users")
            updated_template = self.mongo.update(
                query={"_id": ObjectId(target_template["created_by"]),
                        "template_id": target_template["template_id"]
                    },
                document_data=target_template,
                update_type="push",
                collection_name="users"
            ).get("result")"""
            #updated_template = user_data
            for i in user_data["template_id"]:
                if i == template_id:
                    index = user_data["template_id"].index(i)
                    user_data["stars"][index] += 1
                    break
            updated_template = self.mongo.update(
                query={"_id": ObjectId(user_id)},
                document_data=user_data,
                update_type="set",
                collection_name="users"
            ).get("result")
        else:
            # Increment the `stars` field of the public template document in the `templates` collection
            updated_template = self.mongo.update(
                query={"_id": template_id},
                update_type="inc",
                collection_name="templates",
                document_data={"stars": 1}
            ).get("result")
        # Re-read the template to get the updated data
        updated_template = self.read_template(template_id, user_id=user_id).get("result")
        return updated_template

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
