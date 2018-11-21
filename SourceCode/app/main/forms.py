from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField,PasswordField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError
from ..models import  User, Whiskys

class logInForm(FlaskForm):
	name =StringField('Insert your username: ', validators=[DataRequired()])
	password = PasswordField('Insert your password:', validators=[DataRequired()])
	submit = SubmitField('Sign In')
