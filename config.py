from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "super-secret-key"
app.config["SESSION_COOKIE_HTTPONLY"] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)