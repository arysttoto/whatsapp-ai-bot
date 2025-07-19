import json
from pathlib import Path


# get the resources folder in the tests folder
resources = Path(__file__).parent / "resources"


with open((resources / "text_message_update.json"), "r") as json_file:
    json_message_data = json.load(json_file)

with open(
    (resources / "text_message_update_correct_phone_number.json"), "r"
) as json_file:
    correct_json_message_data = json.load(json_file)


def test_send_message_with_wrong_number(client, webhook_credentials, caplog):
    # testing when a phone number is wrong
    with caplog.at_level("WARNING"):
        response = client.post(
            "/",
            query_string=webhook_credentials,
            json=json_message_data,
        )

    # use caplog to capture apps logs
    logs = caplog.text
    assert response.status_code == 200
    assert "WhatsApp API non-retryable error" in logs


def test_send_message_with_correct_number(client, webhook_credentials):
    # testing when a phone number is correct
    response = client.post(
        "/",
        query_string=webhook_credentials,
        json=correct_json_message_data,
    )

    assert response.status_code == 200
