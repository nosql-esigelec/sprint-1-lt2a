"""
Templates routes.
"""
from fastapi import APIRouter, HTTPException

from src.models.template import TemplateInsertFields, TemplateReadFields
from src.dependencies import get_mongo_db, get_neo4j_db
from src.utils.parsing import parse_mongo_id
from src.services.templates_service import TemplateService


router = APIRouter()
mongo = get_mongo_db()
neo4j = get_neo4j_db()
template_service = TemplateService(mongo, 
                                #    neo4j
                                   )


@router.post("/", response_model=TemplateReadFields)
async def create_template_endpoint(template: TemplateInsertFields):
    """
    Create a new template.
    """
    template_data = template.model_dump()
    created_template_dict = template_service.create_template(template_data).get(
        "result"
    )
    if created_template_dict is None:
        raise HTTPException(status_code=500, detail="template could not be created")
    template_data["tid"] = created_template_dict
    if template_data.get("is_private") is False:
        del template_data["_id"]

    return template_data


@router.get("/", response_model=list[TemplateReadFields])
async def get_templates_endpoint(user_id: str = None):
    """
    Get all public/private templates.
    """
    templates = template_service.list_templates(user_id).get("result")
    if user_id is None:
        templates = parse_mongo_id(templates, "template")
    return templates


@router.get("/{template_id}", response_model=TemplateReadFields)
async def get_template_endpoint(template_id: str, user_id: str = None):
    """
    Get a template by id.
    """
    template = template_service.read_template(template_id, user_id=user_id).get(
        "result"
    )
    if user_id is not None:
        template = template['templates'][0]
    print(f"Template: {template}")
    if user_id is None:
        template = parse_mongo_id(template, "template")
    if template is None:
        raise HTTPException(status_code=404, detail="template not found")
    return template


@router.delete("/{template_id}", response_model=dict)
async def delete_template_endpoint(template_id: str, user_id: str = None):
    """
    Delete a template by id.
    """
    deleted_template = template_service.delete_template(
        template_id, user_id=user_id
    ).get("result")

    # deleted_template = mongo_delete_template(template_id)
    if deleted_template is None:
        raise HTTPException(status_code=404, detail="template not found")
    return {"result": "success", "details": str(deleted_template)}
