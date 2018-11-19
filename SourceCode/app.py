#import bcrypt
from functools import wraps
from flask import Flask, redirect, render_template, request, session, url_for, g
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import sqlite3

app = Flask (__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
#app.secret_key = 'AOZr98j/3yX R~XHH!jmN]LWX,?RT'

#valid_email = 'person@napier.ac.uk'
#valid_pwhash = bcrypt.hashpw('secretpass', bcrypt.gensalt())

class NameForm(FlaskForm):
	name =StringField('Whats is your name?', validators=[DataRequired()])
	submit = SubmitField('Submit')

@app.route('/')
def index():
	return render_template('base.html'),200

@app.route('/signin/')
def signin():
	return render_template('signIn.html'),200

@app.route('/login/')
def login():
    if not session.get('logged_in'):
        return render_template('logIn.html')
    else:
        return "Hello Boss!"

@app.route('/loginAd/', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return login()

@app.route('/aaaa/', methods = ['GET', 'POST'])
def aaaa():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('logIn.html', form = form, name=name)


if __name__==" __main__ ''":
	app.run(host ='0.0.0.0',debug=True)
