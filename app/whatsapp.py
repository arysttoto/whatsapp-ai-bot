class WhatsAppClient:
    def __init__(self, access_token):
        self.access_token = access_token
    # Methods for sending messages, verifying webhooks, etc.
    def verify_webhook(self, request): 
        if request.args.get("hub.verify_token") == self.access_token:
            return request.args.get("hub.challenge")
        return "Authentication failed. Invalid Token."
    def unpack_messages(self, json_request): 
        messages = [] 
        try: 
            messages = json_request["entry"][0]["changes"][0]["messages"] 
        except Exception: 
            pass
        return messages 
    def send_message(seld, message_text): 
        