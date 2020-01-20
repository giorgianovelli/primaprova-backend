from progetto.models import Partita, Punteggio, Domanda, User
from random import seed, sample


# lista punteggi
def getScore(db):
    lista_punteggi = []
    for instance in db.session.query(Partita):
        lista_punteggi.append(Punteggio(instance.user.nome, instance.sessione["punteggio"]))
        # print(instance.user.nome, instance.sessione["punteggio"])  # inserire in un file json TODO
    return lista_punteggi

# lista domande casuali
def getQuiz(db):
    seed()  # int nelle parentesi per generare gli stessi numeri casuali
    sequence = [i for i in range(1, 5)]
    subset = sample(sequence, 2)
    domande_casuali = db.session.query(Domanda).filter(Domanda.idDomanda.in_(subset)).all()
    return [queryd.data for queryd in domande_casuali]


# registrazione utente
def signUp(db, email, nome, password):
    user = db.session.query(User).filter(User.email == email).first()
    if not user:
        new_user = User(email=email, nome=nome)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return True
    else:
        return False


# logIn Utente
def logIn(db, email):
    user = db.session.query(User).filter(User.email == email).first()
    return user


def load_user(db, user_id):
    return db.session.query(User).filter(User.id == user_id).first()

# salvataggioPartita CON TEMPO DI GIOCO



