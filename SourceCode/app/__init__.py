from flask import Flask,current_app,request
from flask_bootstrap import Bootstrap
##Send emails when you register
from flask_mail import Mail
#Get time for tweets
from flask_moment import Moment
#Database
from flask_sqlalchemy import SQLAlchemy
#Getting all the configurations
from config import config
#Using Loging
from flask_login import LoginManager
#Styling text
from flask_pagedown import PageDown
from flask_babel import Babel, lazy_gettext as _l
from elasticsearch import Elasticsearch

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()
babel = Babel()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)
    babel.init_app(app)
    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])
