from flask import render_template, flash, redirect, request
from launchrecord import app
from .forms import LoginForm
from .models import User
from flask_login import login_user


@app.route('/login', methods=['GET', 'POST'])  # view function for login
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.validate_on_submit():
            username = request.form.get('username', None)
            password = request.form.get('password', None)
            remember_me = request.form.get('remember_me', None)
            user = User.query.filter_by(username=username).first()
            if user.verify_password(password):
                login_user(user, remember=remember_me)
                return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

