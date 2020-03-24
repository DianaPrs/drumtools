from webapp.user.models import User 
from webapp.user.forms import LoginForm

from flask_login import current_user, login_user, logout_user 
from flask import Blueprint, render_template, flash, redirect, url_for

blueprint = Blueprint('user', __name__, url_prefix='/users')
 
@blueprint.route("/login")
def login():
    title = "Log in"
    login_form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('login.html', page_title=title, form=login_form)

@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Welcome!')
            return redirect(url_for('account'))

    flash('Incorrect usrname or password')
    return redirect(url_for('user.login'))

@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))