#!/usr/bin/env python3
"""_summary_: all project Imports will be added here
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
#! token = secrets.token_hex(16)
app.config['SECRET_KEY'] = '53665e59e6730130595ea71c41e3eecd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from youtweet import routes