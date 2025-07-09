import requests


class WhatsAppClient:
    def __init__(self, api_url, webhook_verify_token, access_token, phone_number_id):
        self.api_url = api_url 
        self.webhook_verify_token = webhook_verify_token
        self.access_token = access_token
        self.phone_number_id = phone_number_id


    # Methods for sending messages, verifying webhooks, etc.
    def verify_webhook(self, request): 
        if request.args.get("hub.verify_token") == self.webhook_verify_token:
            return request.args.get("hub.challenge") 
        raise PermissionError("Webhook verification token mismatch")
    
    def unpack_messages(self, json_request): 
        messages = [] 
        try: 
            messages = json_request["entry"][0]["changes"][0]["messages"] 
        except Exception: 
            pass
        return messages 
    

    def send_message(self, message_text, receiver_id): 
        url = f"{self.api_url}/{self.phone_number_id}/messages"

        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

        payload = {
            "messaging_product": "whatsapp",
            "to": receiver_id,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": message_text
            }
        }

        response = requests.post(url, headers=headers, json=payload) 