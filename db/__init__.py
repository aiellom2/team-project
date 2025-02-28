from os import environ, path
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Define db here, without initializing it yet.

def create_app():
    # Import Flask inside the function to avoid circular import
    from flask import Flask

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'csc33O'

    # Load environment variables
    load_dotenv('.flaskenv')

    DB_NAME = environ.get('SQLITE_DB')
    if not DB_NAME:
        raise ValueError("Error: SQLITE_DB environment variable is not set!")

    DB_CONFIG_STR = 'sqlite:///' + path.join(path.abspath(path.dirname(__file__)), DB_NAME)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONFIG_STR
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize the db with app here
    db.init_app(app)

    # Import routes and models after initializing app to avoid circular import
    from db import routes, models

    return app, db
