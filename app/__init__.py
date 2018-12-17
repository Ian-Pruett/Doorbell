from flask import Flask
from flask_cors import CORS
from app.config import DefaultConfig


def create_app(config_class=DefaultConfig):
    app = Flask(__name__)
    app.config.from_object(DefaultConfig)
    from app.chatbot.routes import notify
    app.register_blueprint(notify)
    return app