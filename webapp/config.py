import os
from datetime import timedelta

basedir = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
SECRET_KEY = "bjutg75756HHVr;p;.mvc989756rDfcp.HGddrsxn087@$2"

REMEMBER_COOKIE_DURATION = timedelta(days=5)