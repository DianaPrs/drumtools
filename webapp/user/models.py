from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.model import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)
    email = db.Column(db.String(50), unique=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_tutor(self):
        return self.role == 'tutor'

    def __repr__(self):
        return '<User {}>'.format(self.username)

class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    comment = db.Column(db.String, nullable=True)
    notes = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'),
        index=True
    )

    user = relationship('User', backref='UserData')

    def __repr__(self):
        #return 'UserData {}'.format(self.id)
        return f'{self.id}, {self.artist}, {self.title}, {self.comment}'