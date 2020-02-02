from flask.blueprints import Blueprint
from flask import request, jsonify
import json
import flask_praetorian
import progetto.methods as mt

main = Blueprint('main', __name__)


@main.route('/')
def score():
    """

    :return:
    """
    return json.dumps([{"player": user.player, "score": user.score} for user in mt.getRanking()])


@main.route('/login', methods=['POST'])
def login_post():
    """

    :return:
    """
    req_data = request.get_json(force=True)
    email = req_data['email']
    password = req_data['password']
    print(email, password)
    ret = mt.authenticate(email, password)
    print(ret)
    return jsonify(ret), 200


@main.route('/signup', methods=['POST'])
def signup_post():
    """

    :return:
    """
    req_data = request.get_json()
    email = req_data['email']
    name = req_data['name']
    password = req_data['password']
    user = mt.searchUser(email)
    if not user:
        mt.insertUser(email, name, password)
        return json.dumps('User added')  # redirect log in?
    else:
        return json.dumps('User already exists')  # redirect log in?


@main.route('/match', methods=['GET', 'POST'])
@flask_praetorian.auth_required
def match_start():
    """

    :return:
    """
    if request.method == 'GET':
        return json.dumps([queryd.data for queryd in mt.getQuestions()])
    else:
        req_data = request.get_json(force=True)
        if mt.saveMatch(flask_praetorian.current_user().email, req_data):
            return json.dumps('game saved')
        else:
            return json.dumps('error')
