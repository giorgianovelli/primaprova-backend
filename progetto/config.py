class Config(object):
    SECRET_KEY = 'e7b3548dbd5f52720842d2813727a58a221e8a729192ec72'  # da cambiare
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:giorgia@localhost:5432/prova_backend'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_LIFESPAN = {'hours': 24}
    JWT_REFRESH_LIFESPAN = {'days': 30}