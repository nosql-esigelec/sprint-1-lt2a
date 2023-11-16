from pydantic import BaseModel, Field
from typing import Optional


# Union[float, None] = None
class Question(BaseModel):
    id: str
    statement: str
    question_type: str
    section_id: str
    order: int
    required: Optional[bool] = Field(None)
    is_first: Optional[bool] = Field(None)
    options: Optional[list] = Field(None)
