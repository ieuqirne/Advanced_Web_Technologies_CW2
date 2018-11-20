#import bcrypt
import os
from functools import wraps
from flask import Flask, redirect, render_template, request, session, url_for,flash,g
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import sqlite3

basedir= os.path.abspath(os.path.dirname(__file__))

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hard to guess string'

db = SQLAlchemy(app)
#bootstrap = Bootstrap(app)
#app.secret_key = 'AOZr98j/3yX R~XHH!jmN]LWX,?RT'

#valid_email = 'person@napier.ac.uk'
#valid_pwhash = bcrypt.hashpw('secretpass', bcrypt.gensalt())
class User(db.Model):
	_tablename_ = "users"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	password = db.Column(db.String(64))
	firstName = db.Column(db.String(64))
	lastName = db.Column(db.String(64))
	type = db.Column(db.Integer)

	def __repr__(self):
		return '<User %r>' % self.username

class Whiskys(db.Model):
	_tablename_ = "whiskys"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True, index=True)
	distillery = db.Column(db.String(64))
	year = db.Column(db.String(64))
	description = db.Column(db.Text(2000))
	years = db.Column(db.Integer)

	def __repr__(self):
		return '<Whisky %r>' % self.whiskys

#class Inserted(db.Model)
#	_tablename_ = "inserted"
#	id = db.Column(db.Integer, primary_key=True)
#	userId = db.Column(db.Integer,ForeignKey('users.id'))
#	whiskyId = db.Column(db.Integer,ForeignKey('whiskys.id'))
#
#	def __repr__(self):
#		return '<Inserted %i>' % self.inserted

class logInForm(FlaskForm):
	name =StringField('Whats is your name?', validators=[DataRequired()])
	submit = SubmitField('Submit')

@app.route('/')
def index():
	return render_template('base.html'),200

@app.route('/signin/')
def signin():
	return render_template('signIn.html'),200

@app.route('/loginAd/', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return login()

@app.route('/login/', methods = ['GET', 'POST'])
def login():
	form = logInForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.name.data).first()
		if user is None:
			user = User(username=form.name.data)
			db.session.add(user)
			db.session.commit()
			session['known'] = False
		else:
			session['known']= True
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('login'))
	return render_template('logIn.html', form = form, name=session.get('name'),
							known=session.get('known',False))


#Error Handler

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500


if __name__==" __main__ ''":
	app.run(host ='0.0.0.0',debug=True)
