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
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///BLOG?instance=geekintheloftcloud:musicportfolioproject3'
    migration_directory = 'migrations'

