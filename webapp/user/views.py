from webapp.user.models import User 
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.model import db
from flask_login import current_user, login_user, logout_user 
from flask import Blueprint, render_template, flash, redirect, url_for

blueprint = Blueprint('user', __name__, url_prefix='/users')
 
@blueprint.route("/login")
def login():
    title = "Log in"
    login_form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('/user/login.html', page_title=title, form=login_form)

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

@blueprint.route('/signup')
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = "Sign Up"
    form = RegistrationForm()
    return render_template('/user/signup.html', page_title=title, form=form)  

@blueprint.route('process_reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Successful registration')
        return redirect(url_for('user.login'))
    flash('Plese, enter correct data')
    return redirect(url_for('user.signup'))