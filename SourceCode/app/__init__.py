#import bcrypt
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db = SQLAlchemy()

    db.init_app(app)

    #from main import view, models, error
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
#if __name__==" __main__ ''":
#	app.run(host ='0.0.0.0',debug=True)
