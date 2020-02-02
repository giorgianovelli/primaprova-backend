from progetto.database import db
from progetto.guard import guard

from flask import Flask
from flask_cors import CORS
from progetto.config import Config

import progetto.models as mod
from progetto.routes import main


def create_app():
    """Initialize flask app, database and guard.

    :return: app
    """

    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    db.init_app(app)
    guard.init_app(app, mod.User)
    app.register_blueprint(main)
    return app


def setup_database(app):
    """Create database.

    :param app:
    """

    with app.app_context():
        db.create_all()
        prova_user = mod.User(email='beppe@gmail.com', name='beppe')
        prova_user.set_password('prova')
        gio_user = mod.User(email='giorgia@gmail.com', name='giorgia')
        gio_user.set_password('giorgia')
        db.session.add_all([prova_user, gio_user])
        db.session.commit()


if __name__ == "__main__":
    app = create_app()
    # setup_database(app)
    app.run()
