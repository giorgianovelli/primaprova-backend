from progetto.database import db
from progetto.guard import guard

from flask import Flask
from flask_cors import CORS
from progetto.config import Config

import progetto.models as mod
from progetto.routes import main


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    db.init_app(app)
    guard.init_app(app, mod.User)
    app.register_blueprint(main)
    return app


def setup_database(app):
    with app.app_context():
        db.create_all()
        # inser ecc


if __name__ == "__main__":
    app = create_app()
    # chiamo setup_database
    app.run()
