from sqlalchemy import select
from typing import Any
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient

from app.models import Article
from app.tests.app.api.utils import create_article_f
from app.schemas import ArticleCreate
from app.main import app

client = TestClient(app)

def test_add_blog(client: TestClient, db: Session) -> Any:
    
    data_in = ArticleCreate(title="hello", content="Welcome !")
    
    r = client.post("/articles/add", json=data_in.model_dump())
    
    assert r.status_code == 200
    response = r.json()
    assert response["title"] == data_in.title
    assert response["id"] is not None

def test_delete_blog(client: TestClient, db: Session) -> Any:
    
    article = create_article_f(db=db)
    
    r = client.delete(f"/articles/{article.id}")
    
    assert r.status_code == 200
    response = r.json()
    assert response["message"] == "Article supprimé avec succès"
    
    query = select(Article).filter(Article.id==article.id)
    article_db = db.execute(query).scalar_one_or_none()
    assert article_db is None

def test_get_article(client: TestClient, db: Session) -> Any:
    
    article = create_article_f(db=db)
    
    r = client.get(f"/articles/{article.id}")
    
    assert r.status_code == 200
    response = r.json()
    assert response["title"] == article.title