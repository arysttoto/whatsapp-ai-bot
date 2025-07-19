import pytest
from app import create_app
from dotenv import load_dotenv
import os

# Load environment variables from a .env file (e.g., for secret tokens)
load_dotenv()


@pytest.fixture
def client():
    """
    Creates a test client instance of the Flask app.

    This fixture initializes the Flask application using the factory method `create_app`
    and yields a test client that can be used to simulate HTTP requests during testing.

    Usage:
        def test_homepage(client):
            response = client.get("/")
            assert response.status_code == 200
    """
    app = create_app()
    with app.test_client() as client:
        yield client

@pytest.fixture
def webhook_credentials():
    """
    Provides a set of fake query string parameters to simulate a valid webhook verification request.

    These parameters mimic what the WhatsApp API would send during the verification handshake.
    The `hub.verify_token` is loaded from the environment for flexibility, but a default is also set
    for testing purposes.

    Usage:
        def test_webhook_verification(client, webhook_credentials):
            response = client.get("/", query_string=webhook_credentials)
            assert response.status_code == 200
    """
    hub_challenge = "123456"  # Simulated challenge value returned by the app
    query_string = {
        "hub.mode": "subscribe",
        "hub.verify_token": os.getenv(
            "WHATSAPP_WEBHOOK_VERIFY_TOKEN", "your-whatsapp-webhook-verify-token"
        ),
        "hub.challenge": hub_challenge,
    }
    return query_string
