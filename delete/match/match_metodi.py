
from random import seed, sample
from models import Question, User, Match, db


def getQuestions():
    seed()
    sequence = [i for i in range(1, 5)]
    subset = sample(sequence, 2)
    domande_casuali = db.session.query(Question).filter(Question.idQuestion.in_(subset)).all()
    return domande_casuali


def saveMatch(email, data):
    p = db.session.query(User).filter(User.email == email).first()
    if p:
        p.partite.append(Match(sessione=data))
        db.session.commit()
        return True
    else:
        return False
