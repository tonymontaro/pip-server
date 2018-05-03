import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '887ssjdksjsds778lkjhsdf887sdljkshf73hd6shjdhfskdy6hk3hskdyhh'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True