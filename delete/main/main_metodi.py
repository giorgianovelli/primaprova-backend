from progetto.models import Partita, db

class Punteggio(object):
    def __init__(self, giocatore, score):
        self.giocatore = giocatore
        self.score = score


def getRanking():
    lista_punteggi = []
    for instance in db.session.query(Partita):
        lista_punteggi.append(Punteggio(instance.user.email, instance.sessione["punteggio"]))
    return lista_punteggi