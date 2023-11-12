"""
This module contains the Pydantic models for the Project API.
It defines the fields for inserting, updating, reading, and converting projects to and from the database and front-end.
"""

from pydantic import BaseModel, Field
from typing import List, Optional
from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from typing import List, Optional
from bson.objectid import ObjectId

# Union[float, None] = None


from typing import List, Optional
from pydantic import BaseModel, Field

class ProjectFields(BaseModel):
    """
    Represents the fields of a project.

    Attributes:
    -----------
    pid : str, optional
        The project ID.
    created_by : str
        The user who created the project.
    project_name : str
        The name of the project.
    project_type : str
        The type of the project.
    project_architecture : str
        The architecture of the project.
    project_tags : List[str]
        The tags associated with the project.
    """
    pid: Optional[str] = Field(None)
    created_by: str
    project_name: str
    project_type: str
    project_architecture: str
    project_tags: List[str]


from typing import List, Optional
from pydantic import BaseModel, Field

class ProjectOptionalFields(BaseModel):
    """
    Optional fields for a project.

    :param project_name: The name of the project.
    :param project_type: The type of the project.
    :param project_architecture: The architecture of the project.
    :param project_tags: The tags associated with the project.
    """
    project_name: Optional[str] = Field(None)
    project_type: Optional[str] = Field(None)
    project_architecture: Optional[str] = Field(None)
    project_tags: Optional[List[str]] = Field(None)


class ProjectAdvancedFields(BaseModel):
    """
    Represents the advanced fields of a project.

    Attributes:
    -----------
    languages : Optional[List[str]]
        The list of programming languages used in the project.
    language_version : Optional[List[str]]
        The list of versions of the programming languages used in the project.
    frontend_framework : Optional[str]
        The frontend framework used in the project.
    backend_framework : Optional[str]
        The backend framework used in the project.
    add_advanced_configurations : Optional[bool]
        Whether to add advanced configurations to the project.
    additional_configurations : Optional[List[str]]
        The list of additional configurations for the project.
    authentication_type : Optional[str]
        The type of authentication used in the project.
    code_quality_type : Optional[List[str]]
        The list of code quality tools used in the project.
    containerization_type : Optional[str]
        The type of containerization used in the project.
    testing_type : Optional[List[str]]
        The list of testing frameworks used in the project.
    package_manager : Optional[str]
        The package manager used in the project.
    database : Optional[str]
        The database used in the project.
    """
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
    """
    A class representing the fields to be inserted into a project record in the database.
    Inherits from ProjectFields and ProjectAdvancedFields.
    """
    pass


class ProjectUpdateFields(ProjectOptionalFields, ProjectAdvancedFields):
    """
    A class representing the fields that can be updated for a project.

    Inherits from ProjectOptionalFields and ProjectAdvancedFields.
    """
    pass


class ProjectReadFields(ProjectFields, ProjectAdvancedFields):
    """
    A class representing the fields to be read for a project.
    Inherits from ProjectFields and ProjectAdvancedFields.
    """
    pass


from typing import Optional
from pydantic import BaseModel, Field

class ProjectFromFront(BaseModel):
    """
    Represents a project sent from the front-end.

    Attributes:
    -----------
    name : str
        The name of the project.
    project_type : str
        The type of the project.
    tags : str
        The tags associated with the project, separated by commas.
    vcs : Optional[str]
        The version control system used for the project.
    repo : Optional[str]
        The repository URL for the project.
    """
    name: str
    project_type: str
    tags: str
    vcs: Optional[str] = Field(None)
    repo: Optional[str] = Field(None)


from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId

class ProjectFromDB(BaseModel):
    """
    Represents a project stored in the database.

    Attributes:
    -----------
    _id : ObjectId
        The unique identifier of the project.
    name : str
        The name of the project.
    project_type : str
        The type of the project.
    tags : str
        The tags associated with the project, separated by commas.
    vcs : Optional[str]
        The version control system used for the project.
    repo : Optional[str]
        The URL of the project's repository.
    """
    _id: ObjectId
    name: str
    project_type: str
    tags: str
    vcs: Optional[str] = Field(None)
    repo: Optional[str] = Field(None)


class ProjectToDB(BaseModel):
    """
    Represents a project to be stored in the database.

    Attributes:
        name (str): The name of the project.
        project_type (str): The type of the project.
        tags (List[str]): The tags associated with the project.
        vcs (Optional[str]): The version control system used for the project.
        repo (Optional[str]): The repository URL for the project.
    """
    name: str
    project_type: str
    tags: List[str]  # Les tags sont envoyés comme liste de chaînes de caractères
    vcs: Optional[str] = Field(None)
    repo: Optional[str] = Field(None)


class ProjectToFront(BaseModel):
    """
    Represents a project to be sent to the front-end.

    Attributes:
    -----------
    pid : str
        The project ID.
    name : str
        The project name.
    project_type : str
        The project type.
    tags : List[str]
        The project tags as a list of strings.
    vcs : Optional[str], default=None
        The version control system used by the project.
    repo : Optional[str], default=None
        The repository URL of the project.
    """
    pid: str
    name: str
    project_type: str
    tags: List[str]
    vcs: Optional[str] = Field(None)
    repo: Optional[str] = Field(None)
