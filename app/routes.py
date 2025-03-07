import datetime
from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import AdminLoginForm, EmployeeLoginForm, ManagerLoginForm, RequestTypeForm, AddManagerForm, AddEmployeeForm
from app import db
from app.models import User, RequestType
from werkzeug.security import generate_password_hash
import sys


# Employee Routes

@app.route('/employee-main')
def employeeMain():
    return render_template('employee/employee-main.html')


@app.route('/employee-login', methods=['GET', 'POST'])
def employeeLogin():
    form = EmployeeLoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = User.query.filter_by(username=username, role='employee').first()
        
        if user and user.check_password(password):
            flash('Employee Login Successful!', 'success')
            return redirect(url_for('employeeMain'))
        else:
            flash('Invalid username or password!', 'error')            
    return render_template('employee/employee-login.html', form=form)

@app.route('/employee-forgot-password')
def employeeForgotPassword():
    return render_template('employee/employee-forgot-password.html')

# Main managers page route
@app.route('/admin-employees', methods=['GET', 'POST'])
def adminEmployees():
    
    form = AddEmployeeForm()
    
    if form.validate_on_submit():
        # Create new manager
        new_employee = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=generate_password_hash(form.password.data),
            role='employee',
        )
        
        try:
            db.session.add(new_employee)
            db.session.commit()
            flash('Employee added successfully!', 'success')
            return redirect(url_for('adminEmployees'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding employee: {str(e)}', 'error')
    
    # Get all managers
    employees = User.query.filter_by(role='employee').all()
    
    return render_template('admin/admin-employees.html', form=form, employees=employees)

# Delete employee route
@app.route('/admin-delete-employee/<int:employee_id>', methods=['POST'])
def adminDeleteManager(employee_id):
    employee = User.query.get_or_404(employee_id)
    
    if employee.role != 'employee':
        flash('Invalid employee ID', 'error')
        return redirect(url_for('adminEmployees'))
    
    try:
        db.session.delete(employee)
        db.session.commit()
        flash('Employee deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting employee: {str(e)}', 'error')
    
    return redirect(url_for('adminEmployees'))

# Update employee route
@app.route('/admin-update-employee/<int:employee_id>', methods=['POST'])
def adminUpdateEmployee(employee_id):
    employee = User.query.get_or_404(employee_id)
    
    if employee.role != 'employee':
        flash('Invalid employee ID', 'error')
        return redirect(url_for('adminEmployees'))
    
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Check if username already exists for another user
    existing_user = User.query.filter(User.username == username, User.id != employee_id).first()
    if existing_user:
        flash('Username already taken', 'error')
        return redirect(url_for('adminEmployees'))
    
    # Check if email already exists for another user
    existing_email = User.query.filter(User.email == email, User.id != employee_id).first()
    if existing_email:
        flash('Email already registered', 'error')
        return redirect(url_for('adminEmployees'))
    
    try:
        employee.username = username
        employee.email = email
        
        # Only update password if provided
        if password and password.strip():
            employee.password_hash = generate_password_hash(password)
        
        db.session.commit()
        flash('Employee updated successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error updating employee: {str(e)}', 'error')
    
    return redirect(url_for('adminEmployees'))



# Manager Routes

@app.route('/manager-main')
def managerMain():
    return render_template('manager/manager-main.html')

@app.route('/manager-login', methods=['GET', 'POST'])
def managerLogin():
    form = ManagerLoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = User.query.filter_by(username=username, role='manager').first()
        
        if user and user.check_password(password):
            flash('Manager Login Successful!', 'success')
            return redirect(url_for('managerMain'))
        else:
            flash('Invalid username or password!', 'error')
            
    return render_template('manager/manager-login.html', form=form)

@app.route('/manager-forgot-password')
def managerForgotPassword():
    return render_template('manager/manager-forgot-password.html')


# Admin Routes

@app.route('/admin-main', )
def adminMain():
    return render_template('admin/admin-main.html')

@app.route('/admin-request-types', methods=['GET', 'POST'])
def adminRequestTypes():
    form = RequestTypeForm()
    if form.validate_on_submit():
        existing_type = RequestType.query.filter_by(name=form.name.data).first()
        if existing_type:
            flash('This request type already exists!', 'error')
        else:
            new_type = RequestType(name=form.name.data)
            db.session.add(new_type)
            db.session.commit()
            flash('Request type added successfully!', 'success')
            return redirect(url_for('adminRequestTypes'))
    
    request_types = RequestType.query.all()
    return render_template('admin/admin-request-types.html', form=form, request_types=request_types)

@app.route('/admin-delete-request-type/<int:type_id>', methods=['POST'])
def adminDeleteRequestType(type_id):
    request_type = RequestType.query.get_or_404(type_id)
    try:
        db.session.delete(request_type)
        db.session.commit()
        flash('Request type deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error deleting request type!', 'error')
    
    return redirect(url_for('adminRequestTypes'))


@app.route('/admin-login', methods=['GET', 'POST'])
def adminLogin():
    form = AdminLoginForm()
    if form.validate_on_submit():
        # Get user data from form
        username = form.username.data
        password = form.password.data
        
        # Query the database for the user
        user = User.query.filter_by(username=username, role='admin').first()
        
        # Check if user exists and password is correct
        if user and user.check_password(password):
            flash('Admin Login Successful!', 'success')
            return redirect(url_for('adminMain'))
        else:
            flash('Invalid username or password!', 'error')
            
    return render_template('admin/admin-login.html', form=form)

@app.route('/admin-forgot-password',)
def adminForgotPassword():
    return render_template('admin/admin-forgot-password.html')


# Main managers page route
@app.route('/admin-managers', methods=['GET', 'POST'])
def adminManagers():
    
    form = AddManagerForm()
    
    if form.validate_on_submit():
        # Create new manager
        new_manager = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=generate_password_hash(form.password.data),
            role='manager',
        )
        
        try:
            db.session.add(new_manager)
            db.session.commit()
            flash('Manager added successfully!', 'success')
            return redirect(url_for('adminManagers'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding manager: {str(e)}', 'error')
    
    # Get all managers
    managers = User.query.filter_by(role='manager').all()
    
    return render_template('admin/admin-managers.html', form=form, managers=managers)

# Delete manager route
@app.route('/admin-delete-manager/<int:manager_id>', methods=['POST'])
def adminDeleteManager(manager_id):
    manager = User.query.get_or_404(manager_id)
    
    if manager.role != 'manager':
        flash('Invalid manager ID', 'error')
        return redirect(url_for('adminManagers'))
    
    try:
        db.session.delete(manager)
        db.session.commit()
        flash('Manager deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting manager: {str(e)}', 'error')
    
    return redirect(url_for('adminManagers'))

# Update manager route
@app.route('/admin-update-manager/<int:manager_id>', methods=['POST'])
def adminUpdateManager(manager_id):
    manager = User.query.get_or_404(manager_id)
    
    if manager.role != 'manager':
        flash('Invalid manager ID', 'error')
        return redirect(url_for('adminManagers'))
    
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Check if username already exists for another user
    existing_user = User.query.filter(User.username == username, User.id != manager_id).first()
    if existing_user:
        flash('Username already taken', 'error')
        return redirect(url_for('adminManagers'))
    
    # Check if email already exists for another user
    existing_email = User.query.filter(User.email == email, User.id != manager_id).first()
    if existing_email:
        flash('Email already registered', 'error')
        return redirect(url_for('adminManagers'))
    
    try:
        manager.username = username
        manager.email = email
        
        # Only update password if provided
        if password and password.strip():
            manager.password_hash = generate_password_hash(password)
        
        db.session.commit()
        flash('Manager updated successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error updating manager: {str(e)}', 'error')
    
    return redirect(url_for('adminManagers'))

# If you are directly running the application
if __name__ == '__main__':
    app.run(debug=True)
