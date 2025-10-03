from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import Depends
from app.db.config import sessionLocal, Base, engine

Base.metadata.create_all(bind=engine)

def get_db():
    session = sessionLocal()
    with open(session) as db:
        yield db
        

sesionDeps = Annotated[Session, Depends(get_db)]