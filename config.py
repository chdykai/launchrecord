import os


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'launchrecord.db')

CSRF_ENABLED = True
SECRET_KEY = 'chd.ykai@gmail.com'
OPENID_PROVIDERS = [
    {'name': 'google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'yahoo', 'url': 'https://www.me.yahoo.com'}]
