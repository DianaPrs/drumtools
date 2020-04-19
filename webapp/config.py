import os
from datetime import timedelta

basedir = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://atamovich_drum:k15aB&&u@atamovich.beget.tech/atamovich_drum'
SECRET_KEY = "bjutg75756HHVr;p;.mvc989756rDfcp.HGddrsxn087@$2"

REMEMBER_COOKIE_DURATION = timedelta(days=5)

SQLALCHEMY_TRACK_MODIFICATIONS = False