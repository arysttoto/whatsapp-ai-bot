from flask import Blueprint, current_app
from app.whatsapp import WhatsAppClient
from app.ai import AIClient


# Services
whatsapp_client = WhatsAppClient(current_app.config["WHATSAPP_ACCESS_TOKEN"])
ai_client = AIClient(current_app.config["OPENAI_API_KEY"])

# Blueprints
example_blueprint = Blueprint("example_blueprint", __name__)


@example_blueprint.route("/")
def index():
    return "This is an example route"
