from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'c3f098f24c976404335b22ae39d67b92'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rent.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from app import routes
