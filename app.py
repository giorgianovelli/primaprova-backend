from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from config import Config
import methods
import json


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)


@app.route('/')
def score():
    return json.dumps([(user.giocatore, user.score) for user in methods.getScore(db)])

@app.route('/match')
def match():
    return json.dumps(methods.getQuiz(db))



if __name__ == "__main__":
    app.run()
