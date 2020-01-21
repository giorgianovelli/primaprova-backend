from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from progetto.config import Config

import progetto.methods as mt
import json
import flask_praetorian


guard = flask_praetorian.Praetorian()
app = Flask(__name__)

CORS(app)
app.config.from_object(Config)

db = SQLAlchemy(app)

#---------------------------------------------------------------MODELLI----------------------------------------------------------------------

class Partita(db.Model):
    __tablename__ = 'partite'
    idPartita = db.Column(db.Integer, primary_key=True)
    sessione = db.Column(db.JSON)  # Domande, risposte corrette, [punteggio], stato partita
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates="partite")


class Domanda(db.Model):  # da tenere al posto di data_table
    __tablename__ = 'domande'
    idDomanda = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.JSON)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    nome = db.Column(db.String)
    password = db.Column(db.String)
    roles = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True, server_default='true')
    partite = db.relationship("Partita", order_by=Partita.idPartita, back_populates="user")

    def __repr__(self):
        return "<User(email='%s', nome='%s', password='%s')>" % (self.email, self.nome, self.password)

    def set_password(self, password):
        self.password = guard.hash_password(password)

    # def check_password(self, password):
    #     return check_password_hash(self.password, password)

    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    @classmethod
    def lookup(cls, email):
        return cls.query.filter_by(email=email).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id

    def is_valid(self):
        return self.is_active


class Punteggio(object):
    def __init__(self, giocatore, score):
        self.giocatore = giocatore
        self.score = score

#--------------------------------------------------------------------------------------------------------------


guard.init_app(app, User)


@app.route('/')
def score():
    return json.dumps([(user.giocatore, user.score) for user in mt.getScore(db)])


# log out e match con @login_required
# match con metodo get per inviare le domande e post per ricevere i risultati?
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
        return json.dumps('Utente aggiunto')  # redirect log in
    else:
        return json.dumps('Utente esistente')  # redirect sign up


@app.route('/login', methods=['POST'])
def login_post():
    req_data = request.get_json(force=True)
    email = req_data['email']
    password = req_data['password']
    user = guard.authenticate(email, password)
    ret = {'access_token': guard.encode_jwt_token(user)}
    return jsonify(ret), 200


@app.route('/protected')
@flask_praetorian.auth_required
def protected():
    """
    A protected endpoint. The auth_required decorator will require a header
    containing a valid JWT
    .. example::
       $ curl http://localhost:5000/protected -X GET \
         -H "Authorization: Bearer <your_token>"
    """
    return jsonify(message='protected endpoint (allowed user {})'.format(
        flask_praetorian.current_user().username,
    ))


@app.route('/logout')
@flask_praetorian.auth_required
def logout():
    return json.dumps('logout corretto')


if __name__ == "__main__":
    app.run()
