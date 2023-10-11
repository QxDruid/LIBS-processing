import os
class BaseConfig():

    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    TESTING = True

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'db/Nist.db')

class UnittestConfig():
    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    TESTING = True

    SECRET_KEY = 'testconfig'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'