from .database import db
from .guard import guard
from .models import Match, User, Question
from random import seed, sample
from operator import attrgetter
import json


class GameScore(object):
    def __init__(self, player, score):
        """Initialize the GameScore object with the given player value and score value."""

        self.player = player
        self.score = score


def getRanking():  # TODO se un giocatore ha fatto più partite prendere il punteggio migliore
    """Get score game for every player from db and save it in a GameStore object array."""

    score_list = []
    checked = []

    for instance in db.session.query(Match):
        score_list.append(GameScore(instance.user.name, int(instance.session["score"])))

    sorted_list = sorted(score_list, key=attrgetter('score'), reverse=True)
    print([(item.player, item.score) for item in sorted_list])
    """
    for item in sorted_list:
        if item.player not in checked:
            checked.append(item)
    """
    return sorted_list


def authenticate(email, password):
    """Authenticate user, check if the user enters the right email and password.
    Encodes user data into a jwt token that can be used for authorization at protected endpoints.

    :param email: user's email value
    :param password:user's password value
    :return: jwt token
    """

    user = guard.authenticate(email, password)
    ret = {'access_token': guard.encode_jwt_token(user)}
    return ret


def searchUserByEmail(email):
    """Query from db to search the user by email.

    :param email: user's email value
    :return: user
    :rtype: User
    """

    user = db.session.query(User).filter(User.email == email).first()
    return user


def searchUserByName(name):
    """Query from db to search the user by name.

        :param name: user's name value
        :return: user
        :rtype: User
        """
    user = db.session.query(User).filter(User.name == name).first()
    return user


def insertUser(email, name, password):
    """Insert new user in db.

    :param email: user's email value
    :param name:user's password value
    :param password:user's password value
    :return: inserted user
    :rtype: User
    """

    new_user = User(email=email, name=name)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def getQuestions():
    """Get random question from db e return them in an array.

    :return: list of questions
    :rtype: Question
    """
    maxNumQuestion = 10
    seed()
    sequence = []
    for question in db.session.query(Question):
        sequence.append(question.idQuestion)

    if int(len(sequence)/2) > maxNumQuestion:
        num = maxNumQuestion
    else:
        num = int(len(sequence)/2)

    subset = sample(sequence, num)
    random_questions = db.session.query(Question).filter(Question.idQuestion.in_(subset)).all()
    return random_questions


def saveMatch(email, data):
    """Search user by email and save the game in db.

    :param email: user's email value
    :param data: json file with game info
    :return: boolean value to check insert in db
    :rtype: Boolean
    """
    user = db.session.query(User).filter(User.email == email).first()
    if user:
        data_json = json.dumps(data)
        data_dict = json.loads(data_json)
        answers = data_dict["right_answers"]
        if len(answers) > 0:
            score = (len(answers) * 100)/int(data_dict["time"])
            data_dict.update({'score': score})
        else:
            data_dict.update({'score': 0})

        user.games.append(Match(session=data_dict))
        db.session.commit()
        return True
    else:
        return False
