from typing import Any
from fastapi.routing import APIRouter
from fastapi import  HTTPException, status
from app.schemas import ArticleResponse, ArticleCreate, Message
from app.crud import create_article, get_article, delete_article
from app.api.deps import sesionDeps

router = APIRouter(
    prefix='/articles',
    tags=["articles"]
)

@router.post("/add")
def create_article_route(db: sesionDeps,data: ArticleCreate) -> ArticleResponse:
    """
    Crée un article
    """
    return create_article(db=db, data=data)

@router.get("/{article_id}")
def get_article_route(db: sesionDeps, article_id: int) -> ArticleResponse:
    """
    Retourne un article
    """
    article = get_article(db=db, article_id=article_id)
    if article:
        return ArticleResponse.model_validate(article)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Article non trouvé"
    )
    
@router.delete("/{article_id}")
def delete_article_route(db: sesionDeps, article_id: int) -> Message:
    """
    Supprime un article
    """
    article = delete_article(db=db, article_id=article_id)
    if article:
        return Message(message="Article supprimé avec succès")
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Article non trouvé"
    )
    
    