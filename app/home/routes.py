from flask import Blueprint, render_template
#from app.main import bp

home_bp = Blueprint('home_bp', __name__, template_folder='templates')

@home_bp.route('/')
def index():
    #return 'This is The Main Blueprint'
    return render_template('/index.html')