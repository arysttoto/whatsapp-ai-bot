import pytest
from app import create_app
from dotenv import load_dotenv


load_dotenv()

@pytest.fixture 
def client():
    app = create_app()
    with app.test_client() as client:
        yield client 