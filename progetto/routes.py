from flask.blueprints import Blueprint
from flask import request, jsonify, make_response
import json
import flask_praetorian
import progetto.methods as mt

main = Blueprint('main', __name__)


@main.route('/')
def score():
    """Get score game for every played match.

    :return: json with score game for every played match
    """
    return json.dumps([{"player": user.player, "score": user.score} for user in mt.getRanking()])


@main.route('/login', methods=['POST'])
def login_post():
    """Authenticate user.

    :return: jwt token
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
    """User registration.

    :return: response with http code
    """
    req_data = request.get_json()
    email = req_data['email']
    name = req_data['name']
    password = req_data['password']
    if mt.searchUserByEmail(email) or mt.searchUserByName(name):
        data = {'message': 'User already exists', 'code': 'BAD REQUEST'}
        return make_response(jsonify(data), 400)  # redirect log in?
    else:
        new_user = mt.insertUser(email, name, password)  # TODO
        data = {'message': 'User added', 'code': 'SUCCESS'}
        return make_response(jsonify(data), 201)  # redirect log in?


@main.route('/match', methods=['GET', 'POST'])
@flask_praetorian.auth_required
def match_start():
    """Send questions, and receive json file with match info

    :return:
    """
    if request.method == 'GET':
        return json.dumps([queryd.data for queryd in mt.getQuestions()])
    else:
        req_data = request.get_json(force=True)
        if mt.saveMatch(flask_praetorian.current_user().email, req_data):
            return json.dumps('game saved')  # TODO
        else:
            return json.dumps('error')
