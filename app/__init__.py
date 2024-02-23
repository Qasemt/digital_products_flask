from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from .home.routes import home_bp
from .products.routes import products_bp
from .models import db as db


def create_app(debug: bool = False):
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object("config.Config")

    db.init_app(app)  # Add this line Before migrate line
    migrate = Migrate(app, db, render_as_batch=True)
    # Register blueprints here
    app.register_blueprint(home_bp, url_prefix="/")
    app.register_blueprint(products_bp)

    # Create tables in the database if necessary
    with app.app_context():
        db.create_all()
    # handel errors :::::::::::::::::::::::::::::::::::::

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("/404.html"), 404

    @app.errorhandler(403)
    def page_forbidden(error):
        return render_template("/403.html"), 403

    @app.route("/test/")
    def test_page():
        return "<h1>Testing the Flask Application Factory Pattern</h1>"

    # db.session.add(User('admin', 'admin@example.com'))
    # db.session.add(User('guest', 'guest@example.com'))
    # db.session.commit()
    # users = User.query.all()
    # print(users)
    return app
