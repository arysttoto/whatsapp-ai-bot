from flask import Blueprint, current_app, request


# Blueprints
webhook_verification_blueprint = Blueprint("webhook_verification_blueprint", __name__)


@webhook_verification_blueprint.route("/", methods=["GET"])
def webhook_whatsapp():
    """__summary__: Get message from the webhook"""
    # made for whatsapp checking webhooks
    if request.method == "GET":
        return current_app.whatsapp_client.verify_webhook(request) 
    # unpack the webhook notifications
    messages = current_app.whatsapp_client.unpack_messages(request.get_json()) 
    for message in messages: 
        reply = current_app.ai_client.reply_to_message(message) 
        current_app.whatsapp_client.