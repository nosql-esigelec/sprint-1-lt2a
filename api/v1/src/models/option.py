from pydantic import BaseModel, Field
from typing import Optional


# Union[float, None] = None
class Option(BaseModel):
    question_id: str
    text: str
    is_default: Optional[bool] = Field(None)
