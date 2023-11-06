from pydantic import BaseModel, Field
from typing import Optional, List, Union

class TemplateFields(BaseModel):
    tid: Optional[Union[dict,str]] = Field(None)
    created_by: str
    template_name: str
    template_description: str
    is_private: bool
    template_tags: List[str]

class TemplateOptionalFields(BaseModel):
    template_name: Optional[str] = Field(None)
    template_description: Optional[str] = Field(None)
    is_private: Optional[bool] = Field(None)
    template_tags: Optional[List] = Field(None)


class TemplateAdvancedFields(BaseModel):
    template_url: Optional[str]  = Field(None)
    template_tree: Optional[str]  = Field(None)
    relevance_score: Optional[int] = Field(None)

class TemplateInsertFields(TemplateFields, TemplateAdvancedFields):
    pass

class TemplateUpdateFields(TemplateOptionalFields, TemplateAdvancedFields):
    pass

class TemplateReadFields(TemplateFields, TemplateAdvancedFields):
    pass
