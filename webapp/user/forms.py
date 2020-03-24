from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, HiddenField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField('Send', render_kw={"class": "btn btn-primary"})