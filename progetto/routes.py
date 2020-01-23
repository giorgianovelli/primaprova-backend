from flask.blueprints import Blueprint
from flask import request, jsonify
import json
import flask_praetorian
import progetto.metodi as mt

main = Blueprint('main', __name__)


@main.route('/')
def score():
    return json.dumps([(user.giocatore, user.score) for user in mt.getRanking()])


@main.route('/login', methods=['POST'])
def login_post():
    req_data = request.get_json(force=True)
    email = req_data['email']
    password = req_data['password']
    ret = mt.authenticate(email, password)
    return jsonify(ret), 200


@main.route('/signup', methods=['POST'])
def signup_post():
    req_data = request.get_json()
    email = req_data['email']
    nome = req_data['nome']
    password = req_data['password_hash']
    user = mt.searchUser(email)
    if not user:
        mt.insertUser(email, nome, password)
        return json.dumps('Utente aggiunto')  # redirect log in
    else:
        return json.dumps('Utente esistente')  # redirect sign up


@main.route('/match', methods=['GET', 'POST'])
@flask_praetorian.auth_required
def match_start():
    if request.method == 'GET':
        return json.dumps([queryd.data for queryd in mt.getQuestions()])
    else:
        # salva match
        req_data = request.get_json(force=True)
        if mt.saveMatch(flask_praetorian.current_user().email, req_data):
            return json.dumps('partita salvata')
        else:
            return json.dumps('errore')
