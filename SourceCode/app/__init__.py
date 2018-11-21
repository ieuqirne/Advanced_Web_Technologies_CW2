#import bcrypt
from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import DataRequired
from config import Config




#def create_app(config_name):
app = Flask(__name__)
app.config.from_object(Config)
#config.init_app(app)
db = SQLAlchemy()


db.init_app(app)

#from main import view, models, errors


from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

#return app
#if __name__==" __main__ ''":
#	app.run(host ='0.0.0.0',debug=True)
