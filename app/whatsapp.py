"""
WhatsApp Business API Client

This module provides a client for interacting with the WhatsApp Business API.
It handles webhook verification, message sending, and message extraction from
webhook payloads.

The client supports:
- Webhook verification for WhatsApp Business API setup
- Message sending to WhatsApp users
- Message extraction from incoming webhooks
- Phone number formatting (to be implemented)

Example:
    client = WhatsAppClient(
        api_url="https://graph.facebook.com/v17.0",
        webhook_verify_token="your_verify_token",
        access_token="your_access_token",
        phone_number_id="your_phone_number_id"
    )
"""

import requests 
from app.errors import RetryableError

import phonenumbers
from phonenumbers import PhoneNumberFormat, NumberParseException


class WhatsAppClient:
    """
    Client for interacting with WhatsApp Business API.

    This class handles all communication with the WhatsApp Business API including
    webhook verification, message sending, and message extraction from webhook
    payloads.

    Attributes:
        api_url (str): Base URL for WhatsApp Business API
        webhook_verify_token (str): Token for webhook verification
        access_token (str): Access token for API authentication
        phone_number_id (str): WhatsApp phone number ID for sending messages
    """

    def __init__(self, api_url, webhook_verify_token, access_token, phone_number_id):
        """
        Initialize WhatsApp client with API credentials.

        Args:
            api_url (str): Base URL for WhatsApp Business API
                          (e.g., "https://graph.facebook.com/v17.0")
            webhook_verify_token (str): Token used for webhook verification
            access_token (str): Access token for API authentication
            phone_number_id (str): WhatsApp phone number ID for sending messages
        """
        self.api_url = api_url 
        self.webhook_verify_token = webhook_verify_token
        self.access_token = access_token
        self.phone_number_id = phone_number_id

    def verify_webhook(self, request): 
        """
        Verify webhook from WhatsApp Business API.

        This method handles the initial webhook verification process required
        by WhatsApp Business API. It checks the verification token and returns
        the challenge string if valid.

        Args:
            request: Flask request object containing webhook verification data

        Returns:
            str: Challenge string to be returned to WhatsApp for verification

        Raises:
            PermissionError: If verification token doesn't match
        """
        if request.args.get("hub.verify_token") == self.webhook_verify_token:
            return request.args.get("hub.challenge") 
        raise PermissionError("Webhook verification token mismatch")

    def unpack_messages(self, json_request): 
        """
        Extract messages from WhatsApp webhook JSON payload.

        Parses the complex nested JSON structure from WhatsApp webhooks to
        extract individual messages. This handles the specific format used
        by WhatsApp Business API webhooks.

        Args:
            json_request (dict): JSON payload from WhatsApp webhook

        Returns:
            list: List of message objects from the webhook

        Raises:
            RetryableError: If JSON structure is invalid or missing expected fields
        """
        try: 
            return json_request["entry"][0]["changes"][0]["value"]["messages"] 
        except (KeyError, IndexError, TypeError) as error: 
            raise RetryableError(f"Error during json extraction: {error}") 

    def format_wa_phone_number(self, raw_wa_id: str) -> str:
        """
        Format WhatsApp phone number to international format.

        Converts WhatsApp phone number ID to properly formatted international
        phone number format.

        Args:
            raw_wa_id (str): Raw WhatsApp phone number ID

        Returns:
            str: Formatted international phone number

        Note:
            This method is currently a placeholder and needs implementation.
        """
        pass

    def send_message(self, message_text, receiver_phone_number): 
        """
        Send text message to WhatsApp user.

        Sends a text message to a specific WhatsApp user using the WhatsApp
        Business API. Handles API errors and retryable failures appropriately.

        Args:
            message_text (str): Text content to send
            receiver_phone_number (str): Recipient's phone number

        Raises:
            RetryableError: If API returns 5xx errors or network issues occur
        """
        from flask import current_app

        url = f"{self.api_url}/{self.phone_number_id}/messages"

        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

        payload = {
            "messaging_product": "whatsapp",
            "to": receiver_phone_number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": message_text
            }
        }
        try: 
            response = requests.post(url, headers=headers, json=payload) 
            if not response.ok: 
                if 500 <= response.status_code < 600:
                    raise RetryableError(f"WhatsApp API 5xx error: {response.status_code}")

                current_app.logger.warning(
                    f"WhatsApp API non-retryable error ({response.status_code}): {response.text}"
                ) 
        except requests.RequestException as error: 
            raise RetryableError(f"Error sending message: {error}") 
