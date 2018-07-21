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

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User %r>" % self.nickname


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_en = db.Column(db.String(64), unique=True)
    name_zh = db.Column(db.String(64), unique=True)
    abbr = db.Column(db.String(16))
    spaceports = db.relationship('Spaceport', backref=db.backref('country', lazy=True))
    rocket_series = db.relationship('RocketSeries', backref=db.backref('country', lazy=True))


class Spaceport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_en = db.Column(db.String(128), unique=True)
    alias_en = db.Column(db.String(128))
    name_zh = db.Column(db.String(128), unique=True)
    alias_zh = db.Column(db.String(128))
    abbr = db.Column(db.String(16))
    info = db.Column(db.String(2048))
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    records = db.relationship('Record', backref=db.backref('spaceport', lazy=True))


class RocketSeries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_en = db.Column(db.String(128), unique=True)
    name_zh = db.Column(db.String(128), unique=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    rockets = db.relationship('Rocket', backref=db.backref('rocket_series', lazy=True))


class Rocket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_en = db.Column(db.String(64), unique=True)
    name_zh = db.Column(db.String(128), unique=True)
    series_id = db.Column(db.Integer, db.ForeignKey('rocket_series.id'))
    records = db.relationship('Record', backref=db.backref('rocket', lazy=True))


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rocket_id = db.Column(db.Integer, db.ForeignKey('rocket.id'), nullable=False)
    spaceport_id = db.Column(db.Integer, db.ForeignKey('spaceport.id'), nullable=False)
    launch_date = db.Column(db.DateTime, nullable=False)
    payload = db.Column(db.Text, nullable=False)
    result = db.Column(db.String(16))


