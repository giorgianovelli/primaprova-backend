from database import db
from guard import guard

from flask import Flask
from flask_cors import CORS
from config import Config

import models as mod
from routes import main


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

    :param app: current app in use
    """

    with app.app_context():
        db.create_all()
        gio_user = mod.User(email='giorgia@gmail.com', name='giorgia')
        gio_user.set_password('giorgia')
        db.session.add_all([gio_user])
        db.session.commit()


if __name__ == "__main__":
    application = create_app()
    # setup_database(app)
    application.run()
