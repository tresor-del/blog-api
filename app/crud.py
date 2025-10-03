from typing import Any
from sqlalchemy.orm import Session
from app.models import Article
from app.schemas import ArticleCreate, ArticleResponse


def create_article(*, db: Session, data: ArticleCreate) -> ArticleResponse:
    dict_data = data.model_dump()
    print(dict_data)
    validated_data = Article(**dict_data)
    print(validated_data.id)
    db.add(validated_data)
    db.commit()
    db.refresh(validated_data)
    return ArticleResponse.model_validate(validated_data)

def get_article(*, db: Session, article_id: int) -> Article:
    article_db = db.query(Article).where(Article.id == article_id).first()
    return article_db if article_db else  None

def delete_article(*, db:Session, article_id: int) -> bool | None:
    article_db = db.query(Article).where(Article.id == article_id).first()
    if article_db:
        db.delete(article_db)
        db.commit()
        return True
    return None
    