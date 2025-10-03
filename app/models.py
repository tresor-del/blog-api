from sqlalchemy import Column, String, Text, Integer, Boolean
from app.db.config import Base


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), index=True, nullable=False)
    content = Column(String(255), index=True, nullable=False)
    is_active = Column(Boolean, default=True, nullable=True)
