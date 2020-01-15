from models import Partita, Punteggio, Domanda
from random import seed, sample


# lista punteggi
def getScore(db):
    lista_punteggi = []
    for instance in db.session.query(Partita):
        lista_punteggi.append(Punteggio(instance.user.nome, instance.sessione["punteggio"]))
        # print(instance.user.nome, instance.sessione["punteggio"])  # inserire in un file json TODO
    return lista_punteggi


def getQuiz(db):
    # lista domande casuali
    seed()  # int nelle parentesi per generare gli stessi numeri casuali
    sequence = [i for i in range(1, 5)]
    subset = sample(sequence, 2)
    domande_casuali = db.session.query(Domanda).filter(Domanda.idDomanda.in_(subset)).all()
    return ([queryd.data for queryd in domande_casuali])