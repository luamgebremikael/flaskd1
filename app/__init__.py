from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate=Migrate(app,db)
login=LoginManager(app)

login.login_view='/signin'
login.login_message="Please log in first!"

#Import routes at the bottom of page
from app import routes, models