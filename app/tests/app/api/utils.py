from sqlalchemy.orm import Session
from app.schemas import ArticleCreate
from app.crud import create_article


def create_article_f(db: Session):
    
    article = ArticleCreate(
        title="Random article",
        content= "Random content"
    )
    
    return create_article(db=db, data=article)