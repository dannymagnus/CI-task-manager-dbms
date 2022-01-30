#__init__.py runs whenever the directory is imported by another file
#Whatever is in _init__.py gets run so then the folder can be referenced
#normal use would be from taskmanager.models import xxxx
#with __init__.py becomes import taskmanager - then what is in taskmanager can be used
# example here https://www.youtube.com/watch?v=cONc0NcKE7s
#import os so that env variables can be accessed, this wont work once in git.
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#only import the environmental variable if path exists (local environment)
if os.path.exists("env.py"):
    import env  # noqa


#default flask instructions for Flask instatiation
app = Flask(__name__)
#gives flask a secret key to work
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
#this is to check if we are working in local IDE as when deployed we wont be
#accessing our own database but one we make in heroku
if os.environ.get("DEVELOPMENT") == 'True':
    #gives the url for the local database
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    #this is the Heroku database
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

db = SQLAlchemy(app)

#imports the routes py
from taskmanager import routes #noqa