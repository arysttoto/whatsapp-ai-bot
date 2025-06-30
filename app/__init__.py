from flask import Flask


def create_app():
    app = Flask(__name__)
    # Additional setup (register blueprints, config, etc.) goes here 
    return app
