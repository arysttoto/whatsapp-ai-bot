import os

def test_verification_webhook(client):
    """
    Test the webhook verification endpoint.

    This function verifies two scenarios:
    1. When no verification token is provided in the query parameters — should return 403 (forbidden).
    2. When a correct verification token is provided — should return 200 and echo back the 'hub.challenge'.
    """

    # Case 1: Missing verification token — access should be denied.
    response = client.get("/")
    assert response.status_code == 403

    # Case 2: Valid verification token — server should respond with the hub.challenge value.
    hub_challenge = "123456"
    response = client.get(
        "/",
        query_string={
            "hub.mode": "subscribe",
            "hub.verify_token": os.getenv(
                "WHATSAPP_WEBHOOK_VERIFY_TOKEN", "your-whatsapp-webhook-verify-token"
            ),
            "hub.challenge": hub_challenge,
        },
    )

    # Expecting HTTP 200 OK and response body to equal the challenge string
    assert response.status_code == 200
    assert response.data == hub_challenge.encode()
