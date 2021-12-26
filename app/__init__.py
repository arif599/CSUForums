from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

from . import config 
from .views import views
from .auth import auth

def create_app():
    app = Flask(__name__)
    app.config['SECRECT_KEY'] = config.SECRECT_KEY
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
    