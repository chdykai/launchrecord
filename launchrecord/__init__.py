from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin



app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


from launchrecord import views, models
from launchrecord.adminviews import LaunchRecordAdminIndex, LoginModelView

admin = Admin(app, name='luanchrecord-admin', index_view=LaunchRecordAdminIndex(), template_mode='bootstrap3')

admin.add_view(LoginModelView(models.User, db.session))
admin.add_view(LoginModelView(models.Country, db.session))
admin.add_view(LoginModelView(models.Rocket, db.session))
admin.add_view(LoginModelView(models.Record, db.session))
admin.add_view(LoginModelView(models.RocketSeries, db.session))
admin.add_view(LoginModelView(models.Spaceport, db.session))


@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(user_id)

