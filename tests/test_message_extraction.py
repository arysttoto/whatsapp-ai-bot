import json
from pathlib import Path


# get the resources folder in the tests folder
resources = Path(__file__).parent / "resources"

# load json templates
with open((resources / "fake_text_message_update.json"), "r") as json_file:
    json_fake_message_data = json.load(json_file)


with open((resources / "text_message_update.json"), "r") as json_file:
    json_message_data = json.load(json_file)


with open((resources / "other_update.json"), "r") as json_file:
    json_other_update_data = json.load(json_file)


def test_wrong_message_extraction(client, webhook_credentials):
    # testing when a wrong format json is being sent
    response = client.post(
        "/",
        query_string=webhook_credentials,
        json=json_fake_message_data,
    )
    # Error 503 should be displayed, json extraction error
    assert response.status_code == 503
    assert "Error during json extraction: " in response.get_data(as_text=True)


def test_message_extraction(client, webhook_credentials):
    # Check normal message update handlers
    response = client.post(
        "/",
        query_string=webhook_credentials,
        json=json_message_data,
    )
    assert response.status_code == 200


def test_status_update_extraction(client, webhook_credentials):
    # Check normal status update handlers
    response = client.post(
        "/",
        query_string=webhook_credentials,
        json=json_other_update_data,
    )
    assert response.status_code == 200
