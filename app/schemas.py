from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class Article(BaseModel):
    id: int
    title: str
    content: str
    is_active: bool = Field(default=True)
    
    model_config = ConfigDict(from_attributes=True)
    
class ArticleResponse(Article):
    pass

class ArticleCreate(BaseModel):
    title: str
    content: str

class Message(BaseModel):
    message: str