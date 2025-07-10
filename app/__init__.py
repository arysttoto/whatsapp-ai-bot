from flask import Flask, jsonify 
from app.config import Config   
import logging
from app.errors import RetryableError

# Lazy imports are a very good practice in modular Flask applications, don't move them out of the function to avoid circular imports. 
def create_app():
    app = Flask(__name__) 
    app.config.from_object(Config)

    # Logging config
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("logs/app.log")
        ]
    ) 

    # Register global error handlers
    @app.errorhandler(Exception)
    def handle_exception(e):
        app.logger.exception("Unhandled exception:")
        return jsonify({"error": str(e)}), 500

    @app.errorhandler(RetryableError)
    def handle_retryable_error(e):
        app.logger.warning(f"Retryable error: {e}")
        return jsonify({"error": str(e)}), 503

    @app.errorhandler(PermissionError)
    def handle_permission_error(e):
        app.logger.warning(f"Permission error: {e}")
        return jsonify({"error": str(e)}), 403

    @app.errorhandler(ValueError)
    def handle_value_error(e):
        app.logger.warning(f"Validation error: {e}") 
        return jsonify({"error": str(e)}), 400
    
    # Dependency injections, services - AI, Whatsapp client
    from app.whatsapp import WhatsAppClient
    from app.ai import AIClient 

    app.whatsapp_client = WhatsAppClient(app.config["WHATSAPP_API_URL"], app.config["WHATSAPP_WEBHOOK_VERIFY_TOKEN"],
                                          app.config["WHATSAPP_ACCESS_TOKEN"], app.config["WHATSAPP_PHONE_NUMBER_ID"])
    app.ai_client = AIClient(app.config["OPENAI_API_KEY"], app.config["OPENAI_MODEL"], float(app.config["OPENAI_TEMPERATURE"]))  

    # Blueprints/routes creation
    from app.routes import webhook_verification_blueprint  
    app.register_blueprint(webhook_verification_blueprint)   

    return app 
