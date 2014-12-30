"""
settings.py

Configuration for Flask app

"""


class Config(object):
    # Set secret key to use session
    SECRET_KEY = "likelion-flaskr-secret-key"
    debug = False


class Production(Config):
    debug = True
    CSRF_ENABLED = False
    ADMIN = "gabriel6846@gmail.com"
    SQLALCHEMY_DATABASE_URI = 'mysql://jaehee:musicdoc@musicdoc.cwcqbzpenx87.ap-northeast-1.rds.amazonaws.com:3306/musicdoc'
    migration_directory = 'migrations'

