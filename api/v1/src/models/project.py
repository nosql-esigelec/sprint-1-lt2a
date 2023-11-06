from pydantic import BaseModel, Field
from typing import List, Optional
from bson.objectid import ObjectId

# Union[float, None] = None


class ProjectFields(BaseModel):
    pid: Optional[str] = Field(None)
    created_by: str
    project_name: str
    project_type: str
    project_architecture: str
    project_tags: List[
        str
    ]  # Les tags sont envoyés comme liste de chaînes de caractères


class ProjectOptionalFields(BaseModel):
    project_name: Optional[str] = Field(None)
    project_type: Optional[str] = Field(None)
    project_architecture: Optional[str] = Field(None)
    project_tags: Optional[List[str]] = Field(None)


class ProjectAdvancedFields(BaseModel):
    languages: Optional[List[str]] = Field(None)
    language_version: Optional[List[str]] = Field(None)
    frontend_framework: Optional[str] = Field(None)
    backend_framework: Optional[str] = Field(None)
    add_advanced_configurations: Optional[bool] = Field(None)
    additional_configurations: Optional[List[str]] = Field(None)
    authentication_type: Optional[str] = Field(None)
    code_quality_type: Optional[List[str]] = Field(None)
    containerization_type: Optional[str] = Field(None)
    testing_type: Optional[List[str]] = Field(None)
    package_manager: Optional[str] = Field(None)
    database: Optional[str] = Field(None)


class ProjectInsertFields(ProjectFields, ProjectAdvancedFields):
    pass


class ProjectUpdateFields(ProjectOptionalFields, ProjectAdvancedFields):
    pass


class ProjectReadFields(ProjectFields, ProjectAdvancedFields):
    pass


class ProjectFromFront(BaseModel):
    name: str
    project_type: str
    tags: str  # Les tags sont envoyés sous forme de chaîne de caractères séparés par des virgules
    vcs: Optional[str] = Field(None)
    repo: Optional[str] = Field(None)


class ProjectFromDB(BaseModel):
    _id: ObjectId
    name: str
    project_type: str
    tags: str  # Les tags sont envoyés sous forme de chaîne de caractères séparés par des virgules
    vcs: Optional[str] = Field(None)
    repo: Optional[str] = Field(None)


class ProjectToDB(BaseModel):
    name: str
    project_type: str
    tags: List[str]  # Les tags sont envoyés comme liste de chaînes de caractères
    vcs: Optional[str] = Field(None)
    repo: Optional[str] = Field(None)


class ProjectToFront(BaseModel):
    pid: str
    name: str
    project_type: str
    tags: List[str]  # Les tags sont envoyés comme liste de chaînes de caractères
    vcs: Optional[str] = Field(None)
    repo: Optional[str] = Field(None)
