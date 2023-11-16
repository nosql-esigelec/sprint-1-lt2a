# type: ignore
"""
This module contains the ProjectService class which is responsible for managing project operations.
It includes methods to create, read, update, and delete projects, as well as to list projects for a user.
It also includes methods to select a public template for a project and to get recommended templates for a project.
"""
# pylint: disable=W0212
import logging
from typing import Optional

from bson.objectid import ObjectId

from api.v1.src.db.mongo_db import MongoDB
# from src.db.neo4j_db import Neo4jDB
from api.v1.src.utils.handlers import generate_response, handle_db_operations
from api.v1.src.utils.parsing import parse_mongo_id


class ProjectService:
    """
    A class used to represent a Project Service.

    ...

    Attributes
    ----------
    mongo : MongoDB
        An instance of the MongoDB class.

    Methods
    -------
    create_project(project_data: dict) -> str:
        Create a project with the `project_data` object.
    read_project(project_id: str):
        Read a project with the `project_id` object.
    update_project(project_id: str, project_data: dict) -> str:
        Update a project with the `project_data` object.
    delete_project(project_id: str) -> str:
        Delete a project with the `project_id` object.
    list_projects(user_id: str):
        List all projects for a user.
    select_template(project_id: str, template_id: str):
        Select a public template for a project.
    get_recommended_templates(project_id: str):
        Get recommended templates for a project.
    """

    def __init__(self, mongo: MongoDB):
        """
        Initializes a new instance of the ProjectsService class.

        Args:
            mongo (MongoDB, optional): An instance of the MongoDB class. Defaults to None.
            neo4j (Neo4jDB, optional): An instance of the Neo4jDB class. Defaults to None.
        """
        self.mongo = mongo
        # self.neo4j = neo4j

    @handle_db_operations
    def create_project(self, project_data: dict) -> str:
        """
        Create a project with the `project_data` object.

        Args:
            project_data (dict): The project data to be inserted.

        Returns:
            str: The ID of the inserted project.
        """
        if self.mongo is not None:
            insert_result = self.mongo.create(project_data, "projects").get("result")
            project_data = parse_mongo_id(project_data)  # type: ignore
            project_data["id"] = project_data["pid"]
            return str(insert_result)
        else:
            message = f"MongoDB instance is not set."
            return message

    @handle_db_operations
    def read_project(self, project_id: str):
        """
        Read a project with the `project_id` object.

        Args:
            project_id (str): The project id to be read.

        Returns:
            str: The ID of the inserted project.
        """
        if self.mongo is not None:
            project = self.mongo.read(
                query={"_id": ObjectId(project_id)}, collection_name="projects"
            ).get("result")
            return project
        else:
            message = f"MongoDB instance is not set."
            return message

    @handle_db_operations
    def update_project(self, project_id: str, project_data: dict) -> str:
        """
        Update a project with the `project_data` object.

        Args:
            project_id (str): The ID of the project to be updated.
            project_data (dict): The project data to be updated.

        Returns:
            str: The ID of the updated project, or an error message.
        """
        if self.mongo is not None:
            try:
                documents_updated_count = self.mongo.update(
                    query={"_id": ObjectId(project_id)},
                    document_data={"$set": project_data},
                    collection_name="projects",
                )

                if documents_updated_count > 0:
                    return project_id
                else:
                    return "No project was updated. Check if the project ID is correct."

            except Exception as e:
                return f"An error occurred: {str(e)}"
        else:
            return "MongoDB instance is not set."

    @handle_db_operations
    def delete_project(self, project_id: str) -> str:
        """
        Delete a project with the `project_id` object.

        Args:
            project_id (str): The project id to be deleted.

        Returns:
            str: The ID of the deleted project or an error message.
        """
        if self.mongo is not None:
            try:
                # Delete from MongoDB
                documents_deleted_count = self.mongo.delete(
                    query={"_id": ObjectId(project_id)}, collection_name="projects"
                )

                if documents_deleted_count == 0:
                    return "No project was deleted. Check if the project ID is correct."

                # TODO: Delete from Neo4j
                # Add your logic to delete the project from Neo4j here.
                # Example: delete_result_neo4j = self.neo4j.delete_project(project_id)
                # Ensure to handle exceptions and errors appropriately.

                return project_id

            except Exception as e:
                return f"An error occurred: {str(e)}"
        else:
            return "MongoDB instance is not set."

    @handle_db_operations
    def list_projects(self, user_id: str):
        """
        List all projects for a user.

        Args:
            user_id (str): The ID of the user to list projects for.

        Returns:
            list: A list of projects.
        """
        if self.mongo is not None:
            try:
                projects = self.mongo.read(
                    query={"created_by": user_id}, collection_name="projects", many=True
                )
                return projects.get("result")
            except Exception as e:
                return f"An error occurred while listing projects: {e}"
        else:
            return "MongoDB instance is not set."

    @handle_db_operations
    def select_template(self, project_id: str, template_id: str):
        """
        Select a public template for a project.

        Args:
            template_id (str): The ID of the template to select.
            project_id (str): The ID of the project to select the template for.

        Returns:
            str: The ID of the selected template.
        """
        if self.mongo is None:
            raise Exception("MongoDB instance is not set")

        # Check existence of the project
        project = self.mongo.read(query={"_id": project_id}, collection_name="projects")
        if project is None:
            raise Exception("Project not found")

        # Check existence of the template
        template = self.mongo.read(
            query={"_id": template_id, "is_public": True}, collection_name="templates"
        )
        if template is None:
            raise Exception("Template not found or not public")

        # (fixme, neo4j): Create a relationship between the project and the template.
        # You can use the `create` method of the `self.neo4j` instance to create a relationship.
        # For example: self.neo4j.create_relationship(project_id, template_id)
        # relation = self.neo4j.create_relationship(project_id, template_id)
        relation = "TODO"
        return relation

    @handle_db_operations
    def get_recommended_templates(self, project_id: str):
        """
        Get recommended templates for a project.

        Args:
            project_id (str): The ID of the project to get the recommended templates for.

        Returns:
            list: A list of recommended templates.
        """

        # TODO(neo4j): Get recommended templates
        def find_recommended_templates(tx, project_id):
            # (fixme, neo4j): Implement this method to get recommended templates for a project.
            # Write the Cypher query to get recommended templates for a project.
            # Order the templates by the relevance score.
            query = """

            """
            params = {"project_id": project_id}
            result = tx.run(query, params)

            return result.data()

        # templates = self.neo4j.execute_read(find_recommended_templates, project_id=project_id)
        templates = []  # type: ignore
        return templates
