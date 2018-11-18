#import bcrypt
import os
from functools import wraps
from flask import Flask, redirect, render_template, request, session, url_for
from flask import Flask, g
import sqlite3

from flask_sqlalchemy import SQLAlchemy
app = Flask (__name__)


@app.route('/')
def index():
	return render_template('base.html'),200

@app.route('/signin/')
def signin():
	return render_template('signIn.html'),200

@app.route('/login/')
def login():
	return render_template('login.html'),200

if __name__==" __main__ ":
	app.run(host ='0.0.0.0',debug=True)
