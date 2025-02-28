from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Initialize app and db
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Environment configuration (if needed)
load_dotenv('.flaskenv')
DB_NAME = os.environ.get('SQLITE_DB')
basedir = os.path.abspath(os.path.dirname(__file__))

# Database configuration
DB_CONFIG_STR = 'sqlite:///' + os.path.join(basedir, DB_NAME)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONFIG_STR
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database connection
db = SQLAlchemy(app)

# Import routes and models
from main import routes, models  # Adjust if necessary
