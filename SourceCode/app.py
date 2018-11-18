#import bcrypt
from functools import wraps
from flask import Flask, redirect, render_template, request, session, url_for
from flask import Flask, g
import sqlite3

app = Flask (__name__)

#app.secret_key = 'AOZr98j/3yX R~XHH!jmN]LWX,?RT'

#valid_email = 'person@napier.ac.uk'
#valid_pwhash = bcrypt.hashpw('secretpass', bcrypt.gensalt())

db_location = 'var/database.db'

def get_db():
	db = getattr(g, 'db', None)
	if db is None:
		db = sqlite3.connect(db_location)
		g.db = db
	return db

def check_auth(email, password):
	if(email == valid_email and
		valid_pwhash == bcrypt.hashpw(password.encode('utf-8'),
			valid_pwhash)):
			return True
	return False

def requires_login(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		status = session.get('logged_in', False)
		if not status:
			return redirect(url_for('.root'))
		return f(*args, **kwargs)
	return decorated

@app.teardown_appcontext
def close_db_connection(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()

def init_db():
	with app.app_context():
		db = get_db()
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

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


@app.route("/aaa/")
def aaa():
	db = get_db()
	db.cursor().execute('INSERT INTO users VALUES (NULL,"asdasdf","asdf","asdf","asdf","asdf")')
	db.commit()

	page = []
	page.append('<html><ul>')
	sql = "SELECT rowid, * FROM users"
	for row in db.cursor().execute(sql):
		page.append('<li>')
		page.append(str(row))
		page.append('</li>')

	page.append('</ul><html>')

	return ''.join(page)

if __name__==" __main__ ":
	app.run(host ='0.0.0.0',debug=True)
