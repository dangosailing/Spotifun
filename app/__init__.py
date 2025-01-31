from flask import Flask
from config import Config
from app.routes import bp


# Stores environment variables
config = Config()

def create_app():
    spotifun_app = Flask(__name__)
    spotifun_app.config.from_object(Config)
    spotifun_app.register_blueprint(bp)
    
    with spotifun_app.app_context():
        from . import routes, models

    return spotifun_app    
