from .database import db
from .guard import guard
from .models import Partita, User, Domanda
from random import seed, sample


class Punteggio(object):
    def __init__(self, giocatore, score):
        self.giocatore = giocatore
        self.score = score


def getRanking():
    lista_punteggi = []
    for instance in db.session.query(Partita):
        lista_punteggi.append(Punteggio(instance.user.email, instance.sessione["punteggio"]))
    return lista_punteggi


def authenticate(email, password):
    user = guard.authenticate(email, password)
    ret = {'access_token': guard.encode_jwt_token(user)}
    return ret


def searchUser(email):
    user = db.session.query(User).filter(User.email == email).first()
    return user


def insertUser(email, nome, password):
    new_user = User(email=email, nome=nome)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()


def getQuestions():
    seed()
    sequence = [i for i in range(1, 5)]
    subset = sample(sequence, 2)
    domande_casuali = db.session.query(Domanda).filter(Domanda.idDomanda.in_(subset)).all()
    return domande_casuali


def saveMatch(email, data):
    p = db.session.query(User).filter(User.email == email).first()
    if p:
        p.partite.append(Partita(sessione=data))
        db.session.commit()
        return True
    else:
        return False