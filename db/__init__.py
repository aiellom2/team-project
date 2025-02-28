# db/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv('.flaskenv')

# Initialize the database object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'csc33O'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your-database-file.db'  # Example URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the app
    db.init_app(app)

    # You can import routes and models here
    from db import routes, models

    return app
