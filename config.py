import os


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'launchrecord.db')

CSRF_ENABLED = True

SECRET_KEY = 'chd.ykai@gmail.com'

