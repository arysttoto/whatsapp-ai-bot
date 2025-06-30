import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


def test_ping(client):
    response = client.get("/")
    assert response.status_code in (200, 404) 
