from app import app, db
from app.models import User, RequestType, 
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
        password_hash=generate_password_hash('admin123'), 
        role='admin'
    )
    db.session.add(admin)
    
    manager = User(
         username='manager',
         password_hash=generate_password_hash('manager123'),
         role='manager'
     )
    db.session.add(manager)

    employee = User(
         username='employee',
         password_hash=generate_password_hash('employee123'),
         role='employee'
     )
    db.session.add(employee)
    
    # Create initial request types
    initial_request_types = [
        RequestType(name='Time Off'),
        RequestType(name='Equipment Request'),
        RequestType(name='Tech Support'),
        RequestType(name='Vacation Request'),
        RequestType(name='Business Request')
    ]
    
    for request_type in initial_request_types:
        db.session.add(request_type)
    
    # Commit all changes
    db.session.commit()
    print('Database has been either been edited and or created successfully!')