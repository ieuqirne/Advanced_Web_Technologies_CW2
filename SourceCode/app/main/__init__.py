#shows the changes  to the User Model to accommodate password hashing
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models import Permission

#Checking Permissions
@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
