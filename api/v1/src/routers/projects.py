"""
This module contains the API routes for projects. It includes the following routes:
- POST /: Create a new project.
- GET /: Get projects by user id.
- GET /{project_id}: Get a project by id.
- GET /{project_id}/recommended-templates: Get recommended templates for a project.
- PUT /{project_id}: Update a project by id.
- POST /{project_id}/select-template/: Select a template for a project.
- DELETE /{project_id}: Delete a project by id.
"""

from typing import Union
from fastapi import APIRouter, HTTPException
from api.v1.src.models.project import (
    ProjectInsertFields,
    ProjectUpdateFields,
    ProjectReadFields,
    ProjectFields,
)
from api.v1.src.dependencies import get_mongo_db, get_neo4j_db
from api.v1.src.utils.parsing import parse_mongo_id
from api.v1.src.services.projects_service import ProjectService

router = APIRouter()

mongo = get_mongo_db()
neo4j = get_neo4j_db()
project_service = ProjectService(mongo, 
                                #neo4j
)


@router.post("/")
async def create_project_endpoint(project: ProjectInsertFields):
    """
    Create a new project.

    Args:
        project (ProjectInsertFields): The project to be created.

    Returns:
        dict: The created project data.
    Raises:
        HTTPException: If the project could not be created.
    """
    project_data = project.model_dump()
    created_project_id = project_service.create_project(project_data).get("result")
    if created_project_id is None:
        raise HTTPException(status_code=500, detail="Project could not be created")
    # project_data["pid"] = created_project_id

    # del project_data["_id"]
    print(f"The project to return is {project_data}")
    return project_data


@router.get("/", response_model=list[ProjectReadFields])
async def get_projects_endpoint(user_id: str):
    """
    Get projects by user id.

    Args:
        user_id (str): The id of the user.

    Returns:
        list: A list of projects.
    """
    # print("Get projects")
    projects = project_service.list_projects(user_id).get("result")
    projects = parse_mongo_id(projects, "project")
    return projects


@router.get("/{project_id}", response_model=Union[ProjectFields, ProjectReadFields])
async def get_project_endpoint(project_id: str, full: bool = False):
    """
    Get a project by id.

    Args:
        project_id (str): The id of the project to retrieve.
        full (bool, optional): Whether to retrieve the full project or not. Defaults to False.

    Returns:
        Union[ProjectFields, ProjectReadFields]: The retrieved project.
    Raises:
        HTTPException: If the project is not found.
    """
    project = project_service.read_project(project_id).get("result")
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    project = parse_mongo_id(project, "project")
    if full:
        return ProjectReadFields(**project)
    return ProjectFields(**project)

@router.get("/{project_id}/recommended-templates")
async def get_recommended_templates(project_id: str):
    """
    Retrieve recommended templates for a project.

    Args:
        project_id (str): The ID of the project.

    Returns:
        The recommended templates for the project.

    Raises:
        HTTPException: If templates are not found.
    """
    templates = project_service.get_recommended_templates(project_id).get("result") 
    if not templates:
        raise HTTPException(status_code=404, detail="Templates not found")
    return templates

@router.put("/{project_id}", response_model=ProjectReadFields)
async def update_project_endpoint(project_id: str, updated_data: ProjectUpdateFields):
    """
    Update a project by id.

    Args:
        project_id (str): The id of the project to be updated.
        updated_data (ProjectUpdateFields): The updated data for the project.

    Raises:
        HTTPException: If there are no fields to update or if the project is not found.

    Returns:
        ProjectReadFields: The updated project.
    """
    update_dict = {k: v for k, v in updated_data.model_dump().items() if v is not None}
    if not update_dict:
        raise HTTPException(status_code=400, detail="No fields to update")
    updated_result = project_service.update_project(project_id, update_dict).get(
        "result"
    )
    if updated_result is None:
        raise HTTPException(status_code=404, detail="Project not found")
    updated_project = project_service.read_project(project_id).get("result")
    if updated_project is None:
        raise HTTPException(status_code=404, detail="Updated project not found")
    updated_project = parse_mongo_id(updated_project)
    print(f"The updated project is {updated_project}")
    return updated_project

@router.post("/{project_id}/select-template/")
async def project_selected_template(
    project_id: str,  template_id: str
):
    """
    Selects a template for a given project.

    Args:
        project_id (str): The ID of the project to select the template for.
        template_id (str): The ID of the template to select.

    Returns:
        The relation between the project and the selected template.
    """
    relation = project_service.select_template(project_id, template_id).get("result")

    if relation is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return relation

@router.delete("/{project_id}", response_model=dict)
async def delete_project_endpoint(project_id: str):
    """
    Delete a project by id.

    Args:
        project_id (str): The id of the project to be deleted.

    Returns:
        dict: A dictionary containing the result of the operation and details of the deleted project.
    Raises:
        HTTPException: If the project with the given id is not found.
    """
    deleted_project = project_service.delete_project(project_id).get("result")
    if deleted_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"result": "success", "details": str(deleted_project)}
