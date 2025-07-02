from flask import Flask
from app.config import Config
from app.routes import example_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(example_blueprint)

    return app
