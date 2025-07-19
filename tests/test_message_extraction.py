import json
from pathlib import Path

# Define the path to the resources directory within the test suite
resources = Path(__file__).parent / "resources"

# Load test JSON payloads from files in the resources directory

# Payload containing an intentionally malformed or unsupported message format
with open(resources / "fake_text_message_update.json", "r") as json_file:
    json_fake_message_data = json.load(json_file)

# Payload simulating a valid WhatsApp message update
with open(resources / "text_message_update.json", "r") as json_file:
    json_message_data = json.load(json_file)

# Payload simulating a different type of WhatsApp update (e.g., status update)
with open(resources / "other_update.json", "r") as json_file:
    json_other_update_data = json.load(json_file)


def test_wrong_message_extraction(client, webhook_credentials):
    """
    Test the webhook's response to an improperly formatted or unrecognized message payload.

    This test ensures the server correctly identifies invalid JSON structure or unsupported update formats
    and returns a 503 Service Unavailable status with a relevant error message.
    """
    response = client.post(
        "/",
        query_string=webhook_credentials,
        json=json_fake_message_data,
    )
    assert response.status_code == 503
    assert "Error during json extraction: " in response.get_data(as_text=True)


def test_message_extraction(client, webhook_credentials):
    """
    Test the webhook's ability to correctly parse and respond to a standard incoming message update.

    This test validates that a properly structured message payload is handled without error,
    resulting in a 200 OK response.
    """
    response = client.post(
        "/",
        query_string=webhook_credentials,
        json=json_message_data,
    )
    assert response.status_code == 200


def test_status_update_extraction(client, webhook_credentials):
    """
    Test the webhook's ability to handle non-message updates such as delivery or read receipts.

    This test confirms that the application can process alternative update types and still return
    a successful 200 OK response.
    """
    response = client.post(
        "/",
        query_string=webhook_credentials,
        json=json_other_update_data,
    )
    assert response.status_code == 200
