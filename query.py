from app import db
from models import User, Partita, Domanda

if __name__ == '__main__':
    # db.create_all()

    prova_user = User(email='prova@gmail.com', nome='prova')
    # prova_user.set_password('prova')
    gio_user = User(email='giorgia@gmail.com', nome='giorgia')
    # gio_user.set_password('giorgia')
    # db.session.add_all([prova_user, gio_user])

    # db.session.add_all([
    #     Domanda(data={
    #         "testo": "quanto fa 2*2?",
    #         "giusta": "4",
    #         "sbagliate": ["8", "2"]
    #     }),
    #     Domanda(data={
    #        "testo": "quanto fa 2:2?",
    #        "giusta": "1",
    #        "sbagliate": ["4", "2"]
    #    }),
    #     Domanda(data={
    #         "testo": "quanto fa 4*6?",
    #         "giusta": "24",
    #         "sbagliate": ["20", "28"]
    #     }),
    #     Domanda(data={
    #         "testo": "quanto fa 7*4?",
    #         "giusta": "28",
    #         "sbagliate": ["21", "35"]
    #     })
    # ])

    filePartita = {
        "domande": [
            {
                "testo": "quanto fa 7*4?",
                "giusta": "28",
                "sbagliate": ["21", "35"]
            }
        ],
        "risposte_corrette": "28",
        "punteggio": "100",
        "durata_sessione": "15",
        "stato_partita": "terminata"
    }

    # inserimento partita per utente non esistente ok
    jack = User(email='jack@gmail.com', nome='jack')
    # jack.set_password('gjffdd')
    # jack.partite = [Partita(sessione=filePartita)]
    # print([(prova.sessione) for prova in jack.partite])
    # db.session.add(jack)

    # inserimento partita per utente già esistente ok
    # p = db.session.query(User).filter(User.nome == 'prova').first()
    # p.partite.append(Partita(sessione=filePartita))

    # db.session.commit()

    # lista punteggi
    # def getScore():
    #     lista_punteggi = []
    #     for instance in db.session.query(Partita):
    #         lista_punteggi.append(Punteggio(instance.user.nome, instance.sessione["punteggio"]))
    #         # print(instance.user.nome, instance.sessione["punteggio"])  # inserire in un file json TODO
    #     return lista_punteggi




