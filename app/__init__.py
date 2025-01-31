from flask import Flask
from config import Config
from app.routes import bp



class App:
    def ___init__(self):
        self.config = Config()

    def create_app(self):
        spotifun_app = Flask(__name__)
        spotifun_app.config.from_object(self.config)
        spotifun_app.register_blueprint(bp)

        with spotifun_app.app_context():
            from . import routes, models

        return spotifun_app
