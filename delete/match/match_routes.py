from flask.blueprints import Blueprint
from flask import request
from .match_metodi import getQuestions, saveMatch

import json
import flask_praetorian

match = Blueprint('match', __name__)


@match.route('/match', methods=['GET', 'POST'])
@flask_praetorian.auth_required
def match_start():
    if request.method == 'GET':
        return json.dumps([queryd.data for queryd in getQuestions()])
    else:
        # salva match
        req_data = request.get_json(force=True)
        if saveMatch(flask_praetorian.current_user().email, req_data):
            return json.dumps('partita salvata')
        else:
            return json.dumps('errore')
