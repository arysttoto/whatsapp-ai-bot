def test_verification_webhook(client):
    # testing a scenario when webhook verification token is missing
    response = client.get("/")
    assert response.status_code == 403