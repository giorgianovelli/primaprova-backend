from flask.blueprints import Blueprint

from .main_metodi import getRanking
import json

main = Blueprint('main', __name__)

# lista punteggi
@main.route('/')
def score():
    return json.dumps([(user.giocatore, user.score) for user in getRanking()])
