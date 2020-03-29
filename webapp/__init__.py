from flask import Flask, render_template
from flask_migrate import Migrate

from flask_login import LoginManager, current_user, login_required
from flask import Flask, render_template, flash, redirect, url_for
from webapp.user.views import blueprint as user_blueprint
from webapp.admin.views import blueprint as admin_blueprint
from webapp.model import db, Track, Line, Bar, Artist
from webapp.user.models import User



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route("/")
    def index():
        title = "Drumtools"
        track_list = Track.query.order_by(Track.id.desc())[:3]
        return render_template('index.html', page_title=title, track_list=track_list)

    @app.route("/about")
    def about():
        title = "About"
        return render_template('about.html', page_title=title)

    @app.route("/create")
    def creat():
        title = "Create"
        return render_template('create.html', page_title=title)

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
    

    return app
