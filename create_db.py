from app import app, db
from app.models import User
from werkzeug.security import generate_password_hash

# Drop existing tables and create new ones
with app.app_context():
    # This will drop all existing tables
    db.drop_all()
    
    # This will create all tables based on your models
    db.create_all()
    
    # Create admin user
    admin = User(
        username='admin',
        password_hash=generate_password_hash('admin123'),  # Change this to a secure password
        role='admin'
    )
    db.session.add(admin)
    
    # You can add more initial users here if needed
    # Example:
    # manager = User(
    #     username='manager',
    #     password_hash=generate_password_hash('manager123'),
    #     role='manager'
    # )
    # db.session.add(manager)
    
    # Commit all changes
    db.session.commit()
    print('Database recreated and admin user created successfully!')