from app import app, db
from app.models import User, RequestType, OfficeSupply
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


    office_supplies = [
        {"name": "pencil", "price": "$1", "stock": "100"},
        {"name": "chair", "price": "$50", "stock": "16"}
    ]
    
    for supply in office_supplies:
        new_office_supply = OfficeSupply(
            name=supply["name"],
            price=supply["price"],
            stock=supply["stock"]
        )
        db.session.add(new_office_supply)

    
    
    # Create initial request types
    request_types = [
        "Time Off", "Equipment Request", "Tech Support", "Vacation Request", "Business Request"
    ]
    
    for name in request_types:
        db.session.add(RequestType(name=name))
    
    # Commit all changes
    db.session.commit()
    print("Database has been edited and/or created successfully!")
