#import
from flask import Flask
from config import Config
#import blueprint object
from .site.routes import site
# define
app = Flask(__name__)
#register
app.register_blueprint(site)
#config app
app.config.from_object(Config)