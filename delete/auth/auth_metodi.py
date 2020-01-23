# from ..app import db, guard

from progetto.models import User, db, guard


def searchUser(email):
    user = db.session.query(User).filter(User.email == email).first()
    return user


def insertUser(email, nome, password):
    new_user = User(email=email, nome=nome)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()


def authenticate(email, password):
    user = guard.authenticate(email, password)
    ret = {'access_token': guard.encode_jwt_token(user)}
    return ret
