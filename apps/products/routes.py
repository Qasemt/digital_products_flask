from flask import Blueprint, render_template
#from app.main import bp

products_bp = Blueprint('products_bp', __name__, template_folder='templates')

@products_bp.route('/products')
def index():
    #return 'This is The Main Blueprint'
    return render_template('/list_produts.html')