
from random import seed, sample
from progetto.models import Domanda, User, Partita, db


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
