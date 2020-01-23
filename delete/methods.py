"""
from progetto.models import Partita, Domanda, User
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


# auth Utente
def logIn(db, email):
    user = db.session.query(User).filter(User.email == email).first()
    return user

"""

"""
@app.route('/')
def score():
    return json.dumps([(user.giocatore, user.score) for user in mt.getScore(db)])


@app.route('/match', methods=['GET', 'POST'])
@flask_praetorian.auth_required
def match():
    if request.method == 'GET':
        return json.dumps(mt.getQuiz(db))
    else:
        # salva match
        req_data = request.get_json(force=True)
        p = db.session.query(User).filter(User.nome == flask_praetorian.current_user().nome).first()
        p.partite.append(Partita(sessione=req_data))
        db.session.commit()
        return json.dumps('match salvata')


@app.route('/signup', methods=['POST'])
def signup_post():
    req_data = request.get_json()
    email = req_data['email']
    nome = req_data['nome']
    pwd = req_data['password_hash']

    if mt.signUp(db, email, nome, pwd):
        return json.dumps('Utente aggiunto')  # redirect log in
    else:
        return json.dumps('Utente esistente')  # redirect sign up


@app.route('/login', methods=['POST'])
def login_post():
    req_data = request.get_json(force=True)
    email = req_data['email']
    password = req_data['password']
    user = guard.authenticate(email, password)
    ret = {'access_token': guard.encode_jwt_token(user)}
    return jsonify(ret), 200


@app.route('/protected')
@flask_praetorian.auth_required
def protected():

    # A protected endpoint. The auth_required decorator will require a header
    # containing a valid JWT
    # .. example::
    #   $ curl http://localhost:5000/protected -X GET \
    #     -H "Authorization: Bearer <your_token>"

        return jsonify(message='protected endpoint (allowed user {})'.format(
        flask_praetorian.current_user().nome,
    ))



@app.route('/logout')
@flask_praetorian.auth_required
def logout():
    return json.dumps('logout corretto')
"""


