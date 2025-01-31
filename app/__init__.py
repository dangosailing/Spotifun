from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app.routes import bp
from config import Config

db = SQLAlchemy()


class App:
    def ___init__(self):
        pass

    def create_app(self):
        spotifun_app = Flask(__name__)
        # load our config file into the flask config vars
        spotifun_app.config.from_object(Config)
        db.init_app(spotifun_app)
        # register the blueprint w/ routes into the flask app
        spotifun_app.register_blueprint(bp)

        # setup context from which app can get and use vars and methods
        with spotifun_app.app_context():
            # import routes and models into the app context
            from . import routes, models
            db.create_all()

        return spotifun_app
