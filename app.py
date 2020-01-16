from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import Config
import methods as mt
import json


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'route.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_email):
    return mt.load_user(db, user_email)


@app.route('/')
def score():
    return json.dumps([(user.giocatore, user.score) for user in mt.getScore(db)])

# log out e match con @login_required
@app.route('/match')
def match():
    return json.dumps(mt.getQuiz(db))


@app.route('/signup', methods=['POST'])
def signup_post():
    req_data = request.get_json()
    email = req_data['email']
    nome = req_data['nome']
    pwd = req_data['password_hash']

    if mt.signUp(db, email, nome, pwd):
        return 'Utente aggiunto'  # redirect log in
    else:
        return 'Utente esistente'  # redirect sign up


@app.route('/login', methods=['POST'])
def login_post():
    req_data = request.get_json()
    email = req_data['email']
    pwd = req_data['password_hash']
    if mt.logIn(db, email, pwd):
        load_user(email)
        return json.dumps('logIn corretto')  # redirect match
    else:
        return json.dumps('logIn errato')  # redirect logIn o signUp


if __name__ == "__main__":
    app.run()
