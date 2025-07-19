import os
import json
from pathlib import Path


# get the resources folder in the tests folder
resources = Path(__file__).parent / "resources"


def test_message_extraction(client):
    # testing when a wrong format json is being sent
    with open((resources / "fake_text_message_update.json"), "r") as json_file:
        json_data = json.load(json_file)

    hub_challenge = "123456"
    response = client.post(
        "/",
        query_string={
            "hub.mode": "subscribe",
            "hub.verify_token": os.getenv(
                "WHATSAPP_WEBHOOK_VERIFY_TOKEN", "your-whatsapp-webhook-verify-token"
            ),
            "hub.challenge": hub_challenge,
        },
        json=json_data,
    )
    # Error 503 should be displayed, json extraction error
    assert response.status_code == 503
    assert "Error during json extraction: " in str(response.data)
