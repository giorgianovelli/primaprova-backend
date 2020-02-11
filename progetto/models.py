from .database import db
from .guard import guard


class Match(db.Model):
    __tablename__ = 'match'
    idMatch = db.Column(db.Integer, primary_key=True)
    session = db.Column(db.JSON)  # Domande, risposte corrette, [punteggio], stato match
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates="games")


class Question(db.Model):
    __tablename__ = 'questions'
    idQuestion = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.JSON)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    name = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    roles = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True, server_default='true')
    games = db.relationship("Match", order_by=Match.idMatch, back_populates="user")

    def __repr__(self):
        return "<User(email='%s', name='%s', password='%s')>" % (self.email, self.name, self.password)

    def set_password(self, password):
        self.password = guard.hash_password(password)

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



