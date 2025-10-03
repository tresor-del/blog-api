from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.db.config import Base
from app.models import Article
from app.main import app
from app.api.deps import get_db

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(url=DATABASE_URL)

TestingSessionLocal = sessionmaker(bind=engine)

@pytest.fixture(scope="function", autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db():
    session = TestingSessionLocal()
    try: 
        yield session
    finally:
        session.query(Article).delete()
        session.commit()
        session.close()

@pytest.fixture(scope="function")
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            pass
    app.dependency_overrides[get_db] = override_get_db
    
    with TestClient(app) as c:
        yield c