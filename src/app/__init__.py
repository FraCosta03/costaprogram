from flask import Flask
from .config import Config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Config['config_name'])
    return app