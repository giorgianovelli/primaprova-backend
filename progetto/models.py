# from progetto.app import db
# from werkzeug.security import generate_password_hash, check_password_hash
#
#
# class Partita(db.Model):
#     __tablename__ = 'partite'
#     idPartita = db.Column(db.Integer, primary_key=True)
#     sessione = db.Column(db.JSON)  # Domande, risposte corrette, [punteggio], stato partita
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     user = db.relationship("User", back_populates="partite")
#
#
# class Domanda(db.Model):  # da tenere al posto di data_table
#     __tablename__ = 'domande'
#     idDomanda = db.Column(db.Integer, primary_key=True)
#     data = db.Column(db.JSON)
#
#
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String, unique=True)
#     nome = db.Column(db.String)
#     password_hash = db.Column(db.String)
#     is_active = db.Column(db.Boolean, default=True, server_default='true')
#     partite = db.relationship("Partita", order_by=Partita.idPartita, back_populates="user")
#
#     def __repr__(self):
#         return "<User(email='%s', nome='%s', password_hash='%s')>" % (self.email, self.nome, self.password_hash)
#
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)
#
#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
#
#     @classmethod
#     def lookup(cls, email):
#         return cls.query.filter_by(email=email).one_or_none()
#
#     @classmethod
#     def identify(cls, id):
#         return cls.query.get(id)
#
#     @property
#     def identity(self):
#         return self.id
#
#     def is_valid(self):
#         return self.is_active
#
#
# class Punteggio(object):
#     def __init__(self, giocatore, score):
#         self.giocatore = giocatore
#         self.score = score
#
#
