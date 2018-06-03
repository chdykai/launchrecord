import os


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'launchrecord.db')

SQLALCHEMY_TRACK_MODIFICATIONS = True

CSRF_ENABLED = True

SECRET_KEY = 'chd.ykai@gmail.com'

