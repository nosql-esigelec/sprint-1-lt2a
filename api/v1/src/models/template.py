"""
This module defines the models for templates in the API.

The module defines the following models:
- TemplateFields: contains the required fields for a template.
- TemplateOptionalFields: contains the optional fields for a template.
- TemplateAdvancedFields: contains the advanced fields for a template.
- TemplateInsertFields: contains the fields required for inserting a template.
- TemplateUpdateFields: contains the fields required for updating a template.
- TemplateReadFields: contains the fields required for reading a template.
"""
from typing import List, Optional, Union

from pydantic import BaseModel, Field


class TemplateFields(BaseModel):
    """
    TemplateFields model contains the required fields for a template.

    Attributes:
    -----------
    tid : Optional[Union[dict,str]]
        The template id.
    created_by : str
        The user who created the template.
    template_name : str
        The name of the template.
    template_description : str
        The description of the template.
    is_private : bool
        Whether the template is private or not.
    template_tags : List[str]
        The tags associated with the template.
    """

    tid: Optional[Union[dict, str]] = Field(None)
    created_by: str
    template_name: str
    template_description: str
    is_private: bool
    template_tags: List[str]


class TemplateOptionalFields(BaseModel):
    """
    TemplateOptionalFields model contains the optional fields for a template.

    Attributes:
    -----------
    template_name : Optional[str]
        The name of the template.
    template_description : Optional[str]
        The description of the template.
    is_private : Optional[bool]
        Whether the template is private or not.
    template_tags : Optional[List]
        The tags associated with the template.
    """

    template_name: Optional[str] = Field(None)
    template_description: Optional[str] = Field(None)
    is_private: Optional[bool] = Field(None)
    template_tags: Optional[List] = Field(None)


class TemplateAdvancedFields(BaseModel):
    """
    TemplateAdvancedFields model contains the advanced fields for a template.

    Attributes:
    -----------
    template_url : Optional[str]
        The url of the template.
    template_tree : Optional[str]
        The tree of the template.
    relevance_score : Optional[int]
        The relevance score of the template.
    """

    template_url: Optional[str] = Field(None)
    template_tree: Optional[str] = Field(None)
    relevance_score: Optional[int] = Field(None)


class TemplateInsertFields(TemplateFields, TemplateAdvancedFields):
    """
    TemplateInsertFields model contains the fields required for inserting a template.
    Inherits from TemplateFields and TemplateAdvancedFields.
    """

    pass


class TemplateUpdateFields(TemplateOptionalFields, TemplateAdvancedFields):
    """
    TemplateUpdateFields model contains the fields required for updating a template.

    Inherits from TemplateOptionalFields and TemplateAdvancedFields.
    """

    pass


class TemplateReadFields(TemplateFields, TemplateAdvancedFields):
    """
    TemplateReadFields model contains the fields required for reading a template.
    Inherits from TemplateFields and TemplateAdvancedFields.
    """

    pass
