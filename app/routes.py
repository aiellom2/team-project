from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import AdminLoginForm
from app import db
from app.models import User
import sys


# Employee Routes

@app.route('/employee-main')
def employeeMain():
    return render_template('employee/employee-main.html')


@app.route('/employee-login', methods=['GET', 'POST'])
def employeeLogin():
    form = AdminLoginForm()
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


# Manager Routes

@app.route('/manager-main')
def managerMain():
    return render_template('manager/manager-main.html')

@app.route('/manager-login', methods=['GET', 'POST'])
def managerLogin():
    form = AdminLoginForm()
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


@app.route('/admin-main', )
def adminMain():
    return render_template('admin/admin-main.html')

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

# If you are directly running the application
if __name__ == '__main__':
    app.run(debug=True)
