import json
from pathlib import Path


# get the resources folder in the tests folder
resources = Path(__file__).parent / "resources"


with open((resources / "text_message_update.json"), "r") as json_file:
    json_message_data = json.load(json_file)


def test_wrong_message_extraction(client, webhook_credentials):
    # testing when a
    response = client.post(
        "/",
        query_string=webhook_credentials,
        json=json_message_data,
    )

    assert response.status_code == 503
    assert "Error during json extraction: " in response.get_data(as_text=True)
