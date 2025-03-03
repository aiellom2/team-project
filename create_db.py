from app import app, db
from app.models import User
from werkzeug.security import generate_password_hash

# Create the database and tables
with app.app_context():
    db.create_all()
    
    # Check if admin user already exists
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        # Create admin user
        admin = User(
            username='admin',
            password_hash=generate_password_hash('admin123'),  # Change this to a secure password
            role='admin'
        )
        db.session.add(admin)
        db.session.commit()
        print('Admin user created successfully!')
    else:
        print('Admin user already exists.')