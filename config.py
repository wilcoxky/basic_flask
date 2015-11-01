import os


# Default Config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xbf\xb0\x11\xb1\xcd\xf9\xba\x8bp\x0c...'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class TestConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = 'Test Config key'
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
