from .database import db
from .guard import guard
from .models import Match, User, Question
from random import seed, sample
from operator import attrgetter


class GameScore(object):
    def __init__(self, player, score):
        """Initialize the GameScore object with the given player value and score value"""

        self.player = player
        self.score = score


def getRanking():  # TODO se un giocatore ha fatto più partite prendere il punteggio migliore
    """Get score game for every player from db and save it in a GameStore object array."""

    score_list = []
    checked = []

    for instance in db.session.query(Match):
        score_list.append(GameScore(instance.user.name, int(instance.session["punteggio"])))

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

    :param email: user's email value
    :type email:
    :param password:user's password value
    :type password:
    :return:
    :rtype:
    """

    user = guard.authenticate(email, password)
    ret = {'access_token': guard.encode_jwt_token(user)}
    return ret


def searchUser(email):
    """Query from db to search the user by email.

    :param email: user's email value
    :type email:
    :return:
    :rtype:
    """

    user = db.session.query(User).filter(User.email == email).first()
    return user


def insertUser(email, name, password):
    """Insert new user in db.

    :param email: user's email value
    :type email:
    :param name:user's password value
    :type name:
    :param password:user's password value
    :type password:
    :return:
    :rtype:
    """

    new_user = User(email=email, name=name)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()


def getQuestions():
    """Get random question from db e return them in an array.

    :return:
    :rtype:
    """

    seed()
    sequence = []
    for question in db.session.query(Question):
        sequence.append(question.idQuestion)
    subset = sample(sequence, int(len(sequence)/2))
    random_questions = db.session.query(Question).filter(Question.idQuestion.in_(subset)).all()
    return random_questions


def saveMatch(email, data):
    """Search user by email and save the game in db

    :param email: user's email value
    :type email:
    :param data:
    :type data:
    :return:
    :rtype: Boolean
    """

    user = db.session.query(User).filter(User.email == email).first()
    if user:
        user.games.append(Match(session=data))
        db.session.commit()
        return True
    else:
        return False
