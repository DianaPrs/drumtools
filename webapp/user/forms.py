from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, HiddenField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from webapp.user.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField('Send', render_kw={"class": "btn btn-primary"})


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up', render_kw={"class": "btn btn-primary"})

    def validate_username(self, username):
        users_count = User.query.filter_by(username=username.data).count()
        if users_count > 0:
            raise ValidationError('Username already exists')

    def validate_email(self, email):
        users_count = User.query.filter_by(email=email.data).count()
        if users_count > 0:
            raise ValidationError('An account with that email already exists')


class TrackForm(FlaskForm):
    user_id = HiddenField('ID', validators=[DataRequired()])
    artist = StringField('Artist', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    comment = StringField('Comment', validators=[DataRequired()])
    notes = HiddenField('Notes', validators=[DataRequired()])
    submit = SubmitField('Save', render_kw={"class": "btn btn-primary"})

    def validate_user_id(self, user_id):
        if not User.query.get(user_id.data):
            raise ValidationError('No such user here')