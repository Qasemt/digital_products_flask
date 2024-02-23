import datetime

from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)  # Add primary key column
    parent_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    title = db.Column(db.String(50))
    description = db.Column(db.Text)
    avatar = db.Column(db.String(255))
    is_enable = db.Column(db.Boolean, default=True)
    created_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_time = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)
    def __repr__(self):
        return f"<Category {self.title}>"


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)  # Add primary key column
    title = db.Column(db.String(50))
    description = db.Column(db.Text)
    avatar = db.Column(db.String(255))
    is_enable = db.Column(db.Boolean, default=True)
    created_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_time = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

    categories = db.relationship("Category", secondary="product_category", backref="products")

    def __repr__(self):
        return f"<Product {self.title}>"


product_category_association = db.Table(
    "product_category", db.Column("product_id", db.Integer, db.ForeignKey("product.id")), db.Column("category_id", db.Integer, db.ForeignKey("category.id"))
)


class File(db.Model):
    __tablename__ = "file"
    id = db.Column(db.Integer, primary_key=True)  # Add primary key column
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    title = db.Column(db.String(50))
    file_type = db.Column(db.SmallInteger)
    file = db.Column(db.String(255))
    is_enable = db.Column(db.Boolean, default=True)
    created_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_time = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username