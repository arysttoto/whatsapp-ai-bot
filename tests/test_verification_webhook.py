import os 


def test_verification_webhook(client):
    # testing a scenario when webhook verification token is missing
    response = client.get("/")
    assert response.status_code == 403 

    # testing when a verification token is provided 
    hub_challenge = "123456"
    response = client.get("/", query_string={
        "hub.mode": "subscribe",
        "hub.verify_token": os.getenv("WHATSAPP_WEBHOOK_VERIFY_TOKEN", "your-whatsapp-webhook-verify-token"),
        "hub.challenge": hub_challenge
    }) 
    assert response.status_code == 200
    assert response.data == hub_challenge.encode() 