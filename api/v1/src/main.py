from fastapi import APIRouter
from .routers import projects, users, templates#, sections 


router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(projects.router, prefix="/projects", tags=["projects"])
router.include_router(templates.router, prefix="/templates", tags=["templates"])
# router.include_router(sections.router, prefix="/sections", tags=["sections"])
