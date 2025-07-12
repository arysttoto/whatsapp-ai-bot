"""
WhatsApp Webhook Routes

This module handles WhatsApp Business API webhook endpoints for receiving
and processing incoming messages. It provides the main entry point for
WhatsApp message processing and AI response generation.

The webhook endpoint handles:
- Webhook verification (GET requests)
- Message processing (POST requests)
- AI response generation and message sending

Example:
    The webhook endpoint is automatically registered when the Flask app is created.
    WhatsApp will send webhook requests to this endpoint for message delivery.
"""

from flask import Blueprint, current_app, request, jsonify


# Blueprints
webhook_verification_blueprint = Blueprint("webhook_verification_blueprint", __name__)


@webhook_verification_blueprint.route("/", methods=["GET", "POST"])
def webhook_whatsapp():
    """
    Handle WhatsApp Business API webhook requests.

    This endpoint processes both webhook verification (GET) and message
    delivery (POST) requests from WhatsApp Business API.

    GET requests:
        - Used by WhatsApp for initial webhook verification
        - Returns challenge string for verification

    POST requests:
        - Receives incoming messages from WhatsApp users
        - Extracts message content and sender information
        - Generates AI-powered responses
        - Sends responses back to users

    Returns:
        GET: Challenge string for webhook verification
        POST: JSON response with status confirmation

    Note:
        This endpoint processes all message types but currently only handles
        text messages. Other message types (media, location, etc.) are ignored.
    """
    # made for whatsapp checking webhooks
    if request.method == "GET":
        return current_app.whatsapp_client.verify_webhook(request) 

    # unpack the webhook notifications, you can filter by update type later, this boilerplate is only for messages update
    messages = current_app.whatsapp_client.unpack_messages(request.get_json()) 
    for message in messages: 
        parsed_message = message["text"]["body"] 
        reply_message = current_app.ai_client.generate_reply(parsed_message)    
        receiver_phone_number = message["from"]   
        current_app.whatsapp_client.send_message(reply_message, receiver_phone_number)   

    return jsonify({"status": "ok"}), 200 
