
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask import Flask, render_template, flash, redirect, url_for

from webapp.model import db, User, Track, Artist
from webapp.forms import LoginForm


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route("/")
    def index():
        title = "Drumtools"
        return render_template('index.html', page_title=title)

    @app.route("/about")
    def about():
        title = "About"
        return render_template('about.html', page_title=title)

    @app.route("/create")
    def creat():
        title = "Create"
        return render_template('create.html', page_title=title)

    @app.route("/signup")
    def sign_up():
        title = "Sign Up"
        return render_template('signup.html', page_title=title)

    @app.route("/feedback")
    def feedback():
        title = "Feedback"
        return render_template('feedback.html', page_title=title)

    @app.route("/list")
    def full_list():
        title = "List"
        track_list = Track.query.all()
        artist_name = Artist.query.all()
        return render_template('list.html', page_title=title, track_list=track_list, artist_name=artist_name)

    @app.route("/faq")
    def faq():
        title = "FAQ"
        return render_template('faq.html', page_title=title)

    @app.route("/account")
    @login_required
    def account():
        title = "Account"
        return render_template('account.html', page_title=title, name=current_user.username)
    

    @app.route("/login")
    def login():
        title = "Log in"
        login_form = LoginForm()
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        return render_template('login.html', page_title=title, form=login_form)
    
    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Welcome!')
                return redirect(url_for('account'))

        flash('Incorrect usrname or password')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Hello Admin'
        else:
            return 'You are not Admin!'
        

    return app
