from flask import Blueprint, current_app, request


# Blueprints
webhook_verification_blueprint = Blueprint("webhook_verification_blueprint", __name__)


@webhook_verification_blueprint.route("/", methods=["GET"])
def webhook_whatsapp():
    """__summary__: Get message from the webhook"""
    # made for whatsapp checking webhooks
    if request.method == "GET":
        return current_app.whatsapp_client.verify_webhook(request) 
    
    # unpack the webhook notifications, you can filter by update type later, this boilerplate is only for messages update
    messages = current_app.whatsapp_client.unpack_messages(request.get_json()) 
    for message in messages: 
        parsed_message = message["text"]["body"] 
        reply = current_app.ai_client.generate_reply(parsed_message)  
        current_app.whatsapp_client.send_message(reply) 