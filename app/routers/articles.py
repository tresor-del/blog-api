from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Article
from app.utils import read_articles, save_article

router = APIRouter(
    prefix='/articles',
    tags=["articles"],

)


@router.get('/', response_model=List[Article])
def get_articles():
    return read_articles()

@router.post('/', response_model=Article,)
def read_article(article: Article):
    articles = read_articles()
    if any(a['id'] == article.id for a in articles):
        raise HTTPException(status_code=400, detail='Id already exits')
    articles.append(article.dict())
    save_article(articles)
    return articles
