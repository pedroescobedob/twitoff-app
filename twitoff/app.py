from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from twitoff.routes.book_routes import book_routes
from twitoff.routes.home_routes import home_routes

def create_app():
    app = Flask(__name__)

    #configuring the database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///twitoff.db"
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(128))
        author_id = db.Column(db.String(128))

    #registering routes
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)

    return app