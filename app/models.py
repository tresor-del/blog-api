from pydantic import BaseModel, Field
from typing import Optional

class Article(BaseModel):
    id: int
    title: str
    content: str
    is_active: bool = Field(default=True)