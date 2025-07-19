import pytest
from app import create_app
from dotenv import load_dotenv
import os


load_dotenv()


@pytest.fixture 
def client():
    app = create_app()
    with app.test_client() as client:
        yield client 


@pytest.fixture
def webhook_credentials():

    hub_challenge = "123456"
    query_string = {
        "hub.mode": "subscribe",
        "hub.verify_token": os.getenv(
            "WHATSAPP_WEBHOOK_VERIFY_TOKEN", "your-whatsapp-webhook-verify-token"
        ),
        "hub.challenge": hub_challenge,
    }
    return query_string
