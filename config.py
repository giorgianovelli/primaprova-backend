class Config(object):
    SECRET_KEY = 'e7b3548dbd5f52720842d2813727a58a221e8a729192ec72'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:ek0fJ4RAvRCt1EGy2TKc@formulaquizdb.cak5mu0stldg.eu-west-1.rds.amazonaws.com/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_LIFESPAN = {'hours': 24}
    JWT_REFRESH_LIFESPAN = {'days': 30}