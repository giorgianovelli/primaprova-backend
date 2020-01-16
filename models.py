from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


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


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    nome = db.Column(db.String)
    password_hash = db.Column(db.String)
    partite = db.relationship("Partita", order_by=Partita.idPartita, back_populates="user")

    def __repr__(self):
        return "<User(email='%s', nome='%s', password_hash='%s')>" % (self.email, self.nome, self.password_hash)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Punteggio(object):
    def __init__(self, giocatore, score):
        self.giocatore = giocatore
        self.score = score

