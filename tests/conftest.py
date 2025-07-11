import pytest
from fastapi.testclient import TestClient
from fast_zero1.app import app
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from datetime import datetime
from fast_zero1.models import table_registry


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)
@contextmanager
def _mock_db_time_ctx(model, time=datetime(2023, 1, 1)):
    def fake_time_hook(target, mapper, connection):
        if hasattr(target, 'created_at'):
            target.created_at = time

    event.listen(model, 'before_insert', fake_time_hook)
    try:
        yield time
    finally:
        event.remove(model, 'before_insert', fake_time_hook)


# Fixture retorna o context manager renomeado
@pytest.fixture
def mock_db_time():
    return _mock_db_time_ctx




# This fixture provides a TestClient for testing FastAPI applications.
@pytest.fixture
def client():   
 return TestClient(app)