
from flask import Blueprint

bp = Blueprint('home', __name__)

from apps.home import routes