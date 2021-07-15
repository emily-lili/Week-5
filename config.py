import os

# link
basedir = os.path.abspath(os.path.dirname(__file__))

# set up the configuration variables for our flask app
class Config:
    """
        Set config variables for our flask app
        Using environmental variables where necessary
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # stop tracking database changes through sqlalchemy