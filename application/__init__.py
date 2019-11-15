from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Load the config.py file.
    app.config.from_object('config')
    # Load the config.py from the instance folder
    app.config.from_pyfile('config.py', silent=True)

    initialize_extensions(app)
    register_blueprints(app)

    return app

def initialize_extensions(app):
    pass

def register_blueprints(app):
    from .api.views import api

    app.register_blueprint(api, url_prefix='/api')