from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import AdminLoginForm
from app import db
from app.models import User
import sys


# Employee Routes

@app.route('/employee-main')
def employeeMain():
    return render_template('templates/employee/employee-main.html')

@app.route('/employee-login', methods=['GET', 'POST'])
def employeeLogin():
    form = AdminLoginForm()
    if form.validate_on_submit():
        # Authentication logic goes here
        flash('Employee Login Successful!', 'success')
        return redirect(url_for('employeeMain'))
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
        flash('Manager Login Successful!', 'success')
        return redirect(url_for('managerMain'))
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
        flash('DB CHECK LOGIN INFO HERE')
        return redirect(url_for('admin-main.html'))
    return render_template('admin/admin-login.html', form=form)

@app.route('/admin-forgot-password',)
def adminForgotPassword():
    return render_template('admin/admin-forgot-password.html')

# If you are directly running the application
if __name__ == '__main__':
    app.run(debug=True)
