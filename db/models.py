from flask_sqlalchemy import SQLAlchemy

# Import db instance from db/__init__.py without causing circular import
from db import db

# Define the DB schema
class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(64), unique=True, nullable=False)
    population = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return self.city + ': ' + str(self.population)
