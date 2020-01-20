from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from progetto.config import Config
import progetto.methods as mt
import json


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return mt.load_user(db, id)


@app.route('/')
def score():
    return json.dumps([(user.giocatore, user.score) for user in mt.getScore(db)])

# log out e match con @login_required
@app.route('/match')
def match():
    return json.dumps(mt.getQuiz(db))
    # return json.dumps('partita')


@app.route('/signup', methods=['POST'])
def signup_post():
    req_data = request.get_json()
    email = req_data['email']
    nome = req_data['nome']
    pwd = req_data['password_hash']

    if mt.signUp(db, email, nome, pwd):
        return json.dumps('Utente aggiunto')  # redirect log in
    else:
        return json.dumps('Utente esistente')  # redirect sign up


@app.route('/login', methods=['POST'])
def login_post():
    req_data = request.get_json()
    email = req_data['email']
    pwd = req_data['password_hash']
    user = mt.logIn(db, email)
    # print(user)
    if user:
        if user.check_password(pwd):
            print(login_user(user))
            print(current_user.is_authenticated)
            return json.dumps('logIn corretto')

    return json.dumps('logIn non corretto')


@app.route("/hello")
def hello():
    print(current_user.is_authenticated)
    if current_user.is_authenticated:
        return json.dumps('Hello %s!' % current_user.nome)
    else:
        return json.dumps('You are not logged in!')


@app.route('/logout')
@login_required
def logout():
    print(logout_user())
    return json.dumps('logout corretto')


if __name__ == "__main__":
    app.run()
