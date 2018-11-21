from flask import current_app, request, url_for
from . import db

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
