from flask.blueprints import Blueprint
from flask import jsonify, request

import json

from .auth_metodi import searchUser, insertUser, authenticate


auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['POST'])
def signup_post():
    req_data = request.get_json()
    email = req_data['email']
    nome = req_data['nome']
    password = req_data['password_hash']
    user = searchUser(email)
    if not user:
        insertUser(email, nome, password)
        return json.dumps('Utente aggiunto')  # redirect log in
    else:
        return json.dumps('Utente esistente')  # redirect sign up


@auth.route('/login', methods=['POST'])
def login_post():
    req_data = request.get_json(force=True)
    email = req_data['email']
    password = req_data['password']
    ret = authenticate(email, password)
    return jsonify(ret), 200
