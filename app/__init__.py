from flask import Flask   
from app.config import Config   
   

# Lazy imports are a very good practice in modular Flask applications, don't move them out of the function to avoid circular imports. 
def create_app():
    app = Flask(__name__) 
    app.config.from_object(Config)

    # Dependency injections, services - AI, Whatsapp client
    from app.whatsapp import WhatsAppClient
    from app.ai import AIClient 

    app.whatsapp_client = WhatsAppClient(app.config["WHATSAPP_WEBHOOK_VERIFY_TOKEN"])
    app.ai_client = AIClient(app.config["OPENAI_API_KEY"]) 

    # Blueprints/routes creation
    from app.routes import webhook_verification_blueprint  
    app.register_blueprint(webhook_verification_blueprint)   

    return app 
