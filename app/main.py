from app.models import Article
from app.utils import read_articles, save_article

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()


@app.get('/articles', response_model=List[Article])
def get_articles():
    return read_articles()

@app.post('/articles', response_model=Article)
def read_article(article: Article):
    articles = read_articles()
    if any(a['id'] == article.id for a in articles):
        raise HTTPException(status_code=400, detail='Id already exits')
    articles.append(article.dict())
    save_article(articles)
    return article