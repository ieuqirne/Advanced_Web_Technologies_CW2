#shows the changes  to the User Model to accommodate password hashing
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
