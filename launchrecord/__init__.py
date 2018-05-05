import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import basedir
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

admin = Admin(app, name='luanchrecord-admin', template_mode='bootstrap3')

from launchrecord import views, models

admin.add_view(ModelView(models.User, db.session))
