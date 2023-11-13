"""
Project Service
"""
# pylint: disable=W0212
import logging
from bson.objectid import ObjectId
from src.utils.parsing import parse_mongo_id
from src.db.mongo_db import MongoDB
# from src.db.neo4j_db import Neo4jDB
from src.utils.handlers import handle_db_operations

class ProjectService:
    """
    Class to manage project operations.
    """

    def __init__(self, mongo: MongoDB = None, 
                #  neo4j: Neo4jDB = None
                 ): # type: ignore
        self.mongo = mongo
        # self.neo4j = neo4j

    @handle_db_operations
    def create_project(self, project_data: dict):
        """
        Create a project with the `project_data` object.

        Args:
            project_data (dict): The project data to be inserted.

        Returns:
            str: The ID of the inserted project.
        """
        insert_result = self.mongo.create(project_data, "projects").get("result")
        project_data = parse_mongo_id(project_data, "project")
        project_data["id"] = project_data["pid"]


        return str(insert_result)

    @handle_db_operations
    def read_project(self, project_id: str):
        """
        Read a project with the `project_id` object.

        Args:
            project_id (str): The project id to be read.

        Returns:
            str: The ID of the inserted project.
        """
        project = self.mongo.read(
            query={"_id": ObjectId(project_id)}, collection_name="projects"
        ).get("result")
        return project

    @handle_db_operations
    def update_project(self, project_id: str, project_data: dict):
        """
        Update a project with the `project_data` object.

        Args:
            project_data (dict): The project data to be updated.

        Returns:
            str: The ID of the updated project.
        """
        # TODO(mongo): Update project
        # (fixme, mongo): Update the project given their id and the data.
        # Refer to MongoDB documentation: https://docs.mongodb.com/manual/tutorial/update-documents/
        update_result = self.mongo.update(
            query={"_id": ObjectId(project_id)},
            document_data=project_data,
            collection_name="projects",
        ).get("result")
        return str(update_result)

    @handle_db_operations
    def delete_project(self, project_id: str):
        """
        Delete a project with the `project_id` object.

        Args:
            project_id (str): The project id to be deleted.

        Returns:
            str: The ID of the deleted project.
        """
        # TODO(mongo): Delete Project
        # (fixme, mongo): Implement this method to delete a project from mongo.
        # (fixme, neo4j):Also, delete the project from Neo4j.
        # Refer to MongoDB documentation: https://docs.mongodb.com/manual/tutorial/remove-documents/
        delete_result = self.mongo.delete(
            query={"_id": ObjectId(project_id)}, collection_name="projects"
        ).get("result")

        return str(delete_result)

    @handle_db_operations
    def list_projects(self, user_id: str):
        """
        List all projects for a user.

        Args:
            user_id (str): The ID of the user to list projects for.

        Returns:
            list: A list of projects.
        """
        #TODO(mongo): List projects
        # (fixme, mongo): Implement the listing of projects for a user.
        # You can use the `read` method of the MongoDB class.
        # Refer to MongoDB documentation: https://docs.mongodb.com/manual/tutorial/query-documents/
        projects = self.mongo.read(
            query={"created_by": user_id}, collection_name="projects", many=True
        ).get("result")
        return projects


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
        # TODO(both): Select Template
        # (fixme, mongo): Check the existence of the project and the template.
    
        project = "TODO"
        if project is None:
            raise Exception("Project not found")
        template = "TODO"
        if template is None:
            raise Exception("Template not found")
        
        # (fixme, neo4j): Create a relationship between the project and the template.
        # You can use the `create` method of the `self.neo4j` instance to create a relationship.
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
            params = {'project_id': project_id}
            result = tx.run(query, params)
            
            return result.data()

        templates = self.neo4j.execute_read(find_recommended_templates, project_id=project_id)
        return templates


