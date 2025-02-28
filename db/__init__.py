def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'csc33O'

    from os import environ, path
    from dotenv import load_dotenv

    # Load environment variables
    load_dotenv('.flaskenv')

    DB_NAME = environ.get('SQLITE_DB')
    if not DB_NAME:
        raise ValueError("Error: SQLITE_DB environment variable is not set!")

    DB_CONFIG_STR = 'sqlite:///' + path.join(path.abspath(path.dirname(__file__)), DB_NAME)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONFIG_STR
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Create database connection
    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy(app)

    # Import routes after app is created
    from db import routes, models

    return app, db

app, db = create_app()
