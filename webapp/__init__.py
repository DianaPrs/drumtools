from flask import Flask, render_template
from webapp.model import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

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

    @app.route("/list")
    def full_list():
        title = "List"
        return render_template('list.html', page_title=title)

    @app.route("/faq")
    def faq():
        title = "FAQ"
        return render_template('faq.html', page_title=title)

    @app.route("/login")
    def log_in():
        title = "Log in"
        return render_template('login.html', page_title=title)

    return app
