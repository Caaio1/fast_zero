import pytest
from fastapi.testclient import TestClient
from fast_zero1.app import app
@pytest.fixture
def client():   
 return TestClient(app)