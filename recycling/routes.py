from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, current_user, login_required
from app.models import User
from app import db
from app.forms import RegistrationForm
from datetime import datetime
from app.forms import EditProfileForm


#Error Handler
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500
