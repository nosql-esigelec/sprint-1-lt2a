from pydantic import BaseModel, Field
from typing import Optional


# Union[float, None] = None
class Section(BaseModel):
    id: str
    name: str
    order: int
    description: str
    is_conditional: bool
