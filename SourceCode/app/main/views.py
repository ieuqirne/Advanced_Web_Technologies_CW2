from datetime import datetime
from flask import render_template, session, redirect, url_for
from .forms import logInForm
from .. import db
from ..models import User

@main.route('/')
def index():
	return render_template('base.html'),200

@main.route('/signin/')
def signin():
	return render_template('signIn.html'),200

@main.route('/loginAd/', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return login()

@main.route('/login/', methods = ['GET', 'POST'])
def login():
	form = logInForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.name.data).first()
		password = User.query.filter_by(password=form.password.data).first()
		if user is None:
			user = User(username=form.name.data)
			password = User(password=form.password.data)
			db.session.add(user)
			db.session.add(password)
			db.session.commit()
			session['known'] = False
		else:
			session['known']= True
		session['name'] = form.name.data
		form.name.data = ''
		form.password.data = ''
		return redirect(url_for('.login'))
	return render_template('logIn.html', form = form, name=session.get('name'),
							known=session.get('known',False))
