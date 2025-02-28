from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import AdminLoginForm
from app import db
from app.models import User
import sys


# Employee Routes

@app.route('/employee-main')
def employeeMainPage():
    return render_template('templates/employee/employee-main.html')

@app.route('/employee-login', methods=['GET', 'POST'], endpoint='employeeLoginPage')
def employeeLoginPage():
    form = AdminLoginForm()
    if form.validate_on_submit():
        # Authentication logic goes here
        flash('Employee Login Successful!', 'success')
        return redirect(url_for('employeeMainPage'))
    return render_template('templates/employee/employee-login.html', form=form)

@app.route('/employee-forgot-password', endpoint='employeeForgotPasswordPage')
def employeeForgotPasswordPage():
    return render_template('templates/employee/employee-forgot-password.html')


# Manager Routes

@app.route('/manager-main')
def managerMainPage():
    return render_template('templates/manager/manager-main.html')

@app.route('/manager-login', methods=['GET', 'POST'], endpoint='managerLoginPage')
def managerLoginPage():
    form = AdminLoginForm()
    if form.validate_on_submit():
        flash('Manager Login Successful!', 'success')
        return redirect(url_for('managerMainPage'))
    return render_template('templates/manager/manager-login.html', form=form)

@app.route('/manager-forgot-password', endpoint='managerForgotPasswordPage')
def managerForgotPasswordPage():
    return render_template('templates/manager/manager-forgot-password.html')


@app.route('/admin-main', endpoint='adminMainPage')
def adminMainPage():
    return render_template('templates/admin/admin-main.html')

@app.route('/admin-login', methods=['GET', 'POST'])
def adminLogin():
    form = AdminLoginForm()
    if form.validate_on_submit():
        flash('DB CHECK LOGIN INFO HERE')
        return redirect(url_for('admin-main.html'))
    return render_template('admin/admin-login.html', form=form)

@app.route('/admin-forgot-password', endpoint='adminForgotPasswordPage')
def adminForgotPasswordPage():
    return render_template('templates/admin/admin-forgot-password.html')

# If you are directly running the application
if __name__ == '__main__':
    app.run(debug=True)
