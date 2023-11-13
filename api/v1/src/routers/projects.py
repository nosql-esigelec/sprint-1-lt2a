"""
Project routes.
"""
from typing import Union
from fastapi import APIRouter, HTTPException
from src.models.project import (
    ProjectInsertFields,
    ProjectUpdateFields,
    ProjectReadFields,
    ProjectFields,
)
from src.dependencies import get_mongo_db, get_neo4j_db
from src.utils.parsing import parse_mongo_id
from src.services.projects_service import ProjectService

router = APIRouter()

mongo = get_mongo_db()
neo4j = get_neo4j_db()
project_service = ProjectService(mongo, 
                                #  neo4j
                                 )


@router.post("/")
async def create_project_endpoint(project: ProjectInsertFields):
    """
    Create a new project.
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
    """
    # print("Get projects")
    projects = project_service.list_projects(user_id).get("result")
    projects = parse_mongo_id(projects, "project")
    return projects


@router.get("/{project_id}", response_model=Union[ProjectFields, ProjectReadFields])
async def get_project_endpoint(project_id: str, full: bool = False):
    """
    Get a project by id.
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
    templates = project_service.get_recommended_templates(project_id).get("result") 
   
    if not templates:
        raise HTTPException(status_code=404, detail="Templates not found")
    return templates

@router.put("/{project_id}", response_model=ProjectReadFields)
async def update_project_endpoint(project_id: str, updated_data: ProjectUpdateFields):
    """
    Update a project by id.
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
    relation = project_service.select_template(project_id, template_id).get("result")

    if relation is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return relation

@router.delete("/{project_id}", response_model=dict)
async def delete_project_endpoint(project_id: str):
    """
    Delete a project by id.
    """
    deleted_project = project_service.delete_project(project_id).get("result")
    if deleted_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"result": "success", "details": str(deleted_project)}
