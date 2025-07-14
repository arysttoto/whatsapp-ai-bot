# Making sure correct root folder is specified, so app package will be seen 
import pytest
from app import create_app
from dotenv import load_dotenv


load_dotenv()

@pytest.fixture 
def client():
    app = create_app()
    with app.test_client() as client:
        yield client 