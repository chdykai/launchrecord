from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, login_user
from flask import request, redirect, url_for, flash
from .forms import LoginForm
from .models import User


class LaunchRecordAdminIndex(AdminIndexView):
    """
    自定义数据管理后台的Index页面，主要是为了增加管理员登陆页面，
    """
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('.login'))
        return super(LaunchRecordAdminIndex, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login(self):
        form = LoginForm(request.form)
        if form.validate_on_submit():
            username = request.form.get('username', None)
            password = request.form.get('password', None)
            remember_me = request.form.get('remember_me', None)
            user = User.query.filter_by(username=username).first()
            if user is None:
                flash('Invalid Username')
                return redirect(url_for('.index'))
            if user.check_password(password):
                login_user(user, remember=remember_me)
        if current_user.is_authenticated:
            return redirect(url_for('.index'))

        # 需要将form传递到template中，这里用到了AdminIndexView的特殊参数
        self._template_args['form'] = form
        return super(LaunchRecordAdminIndex, self).index()


class LoginModelView(ModelView):
    """
    自定义Model的数据管理页面，主要是为了增加管理权限
    """
    def is_accessible(self):
        return current_user.is_authenticated

