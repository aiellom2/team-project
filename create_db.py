from app import app, db
from app.models import User, RequestType
from werkzeug.security import generate_password_hash

# Drop existing tables and create new ones
with app.app_context():
    # Drop all existing tables
    db.drop_all()
    
    # Create all tables based on your models
    db.create_all()
    
    # Create default users with emails
    users = [
        {"username": "admin", "email": "admin@example.com", "password": "admin123", "role": "admin"},
        {"username": "manager", "email": "manager@example.com", "password": "manager123", "role": "manager"},
        {"username": "employee", "email": "employee@example.com", "password": "employee123", "role": "employee"},
    ]
    
    for user in users:
        new_user = User(
            username=user["username"],
            email=user["email"],
            password_hash=generate_password_hash(user["password"]),
            role=user["role"]
        )
        db.session.add(new_user)
    
    # Create initial request types
    request_types = [
        "Time Off", "Equipment Request", "Tech Support", "Vacation Request", "Business Request"
    ]
    
    for name in request_types:
        db.session.add(RequestType(name=name))
    
    # Commit all changes
    db.session.commit()
    print("Database has been edited and/or created successfully!")
