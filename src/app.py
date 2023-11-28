from flask import Flask


def init_app():
    """Construindo o app"""
    app = Flask(__name__)
    return app
