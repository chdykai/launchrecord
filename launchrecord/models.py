from launchrecord import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    # def __init__(self, username):
    #     self.username = username

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String())

    @property
    def password(self):
        """property装饰器用来将password函数转化为变量，同时还生成了password.setter装饰器"""
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(self, password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User %r>" % self.nickname


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    rockets = db.relationship('Rocket', backref='country', lazy=True)


class Rocket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    records = db.relationship('Record', backref='rocket', lazy=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rocket_id = db.Column(db.Integer, db.ForeignKey('rocket.id'), nullable=False)
    launch_date = db.Column(db.DateTime, nullable=False)
    payload = db.Column(db.Text, nullable=False)
    spaceport = db.Column(db.String(128), nullable=False)
    # country_id = db.Column(db.Integer, db.ForeignKey('rocket.country_id'), nullable=False)  # 这种调用父辈关系不知道行不行的通

