
from flask import Flask, render_template
from config import Config
from app.home.routes import  home_bp
from app.products.routes import products_bp
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register blueprints here
   

    app.register_blueprint(home_bp, url_prefix='/')
    app.register_blueprint(products_bp)



    @app.errorhandler(404)
    def page_not_found(error):
     return render_template("/404.html"), 404
    

    @app.errorhandler(403)
    def page_forbidden(error):
     return render_template("/403.html"), 403
    
    
    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app