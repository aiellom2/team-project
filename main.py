import json
import sys

from flask import Flask, render_template, request, redirect, url_for, flash



app = Flask(__name__)


    
# employee Routes

# employee Main
@app.route('/employee-main')
def employeeMainPage():
    return render_template('employee/employee-main.html')

# employee Login
@app.route('/employee-login', endpoint='employeeLoginPage')
def employeeLoginPage():
    return render_template('employee/employee-login.html')


# employee Forgot Password
@app.route('/employee-forgot-password', endpoint='employeeForgotPasswordPage')
def employeeForgotPasswordPage():
    return render_template('employee/employee-forgot-password.html')


# manager Routes

# manager Main
@app.route('/manager-main')
def managerMainPage():
    return render_template('manager/manager-main.html')

# manager Login
@app.route('/manager-login', endpoint='managerLoginPage')
def managerLoginPage():
    return render_template('manager/manager-login.html')


# manager Forgot Password
@app.route('/manager-forgot-password', endpoint='managerForgotPasswordPage')
def managerForgotPasswordPage():
    return render_template('manager/manager-forgot-password.html')


# Admin Routes

# admin Main 
@app.route('/admin-main', endpoint='adminMainPage')
def adminMainPage():
    return render_template('admin/admin-main.html')

# admin Login
@app.route('/admin-login', endpoint='adminLoginPage')
def adminLoginPage():
    return render_template('admin/admin-login.html')

# admin Forgot Password
@app.route('/admin-forgot-password', endpoint='adminForgotPasswordPage')
def adminForgotPasswordPage():
    return render_template('admin/admin-forgot-password.html')
 
