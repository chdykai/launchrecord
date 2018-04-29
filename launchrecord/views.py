from flask import render_template, flash, redirect
from launchrecord import app
from .forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])  # view function for login
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

