from flask import Blueprint, current_app


# Blueprints
example_blueprint = Blueprint("example_blueprint", __name__)


@example_blueprint.route("/")
def index():
    return "This is an example route"
