import sys
from flask import Flask, render_template, request, redirect, url_for, flash
from db.forms import AdminLoginForm

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'your_secret_key'  # Required for CSRF protection

# Employee Routes

@app.route('/employee-main')
def employeeMainPage():
    return render_template('employee/employee-main.html')

@app.route('/employee-login', methods=['GET', 'POST'], endpoint='employeeLoginPage')
def employeeLoginPage():
    form = AdminLoginForm()
    if form.validate_on_submit():
        # Authentication logic goes here
        flash('Employee Login Successful!', 'success')
        return redirect(url_for('employeeMainPage'))
    return render_template('employee/employee-login.html', form=form)

@app.route('/employee-forgot-password', endpoint='employeeForgotPasswordPage')
def employeeForgotPasswordPage():
    return render_template('employee/employee-forgot-password.html')


# Manager Routes

@app.route('/manager-main')
def managerMainPage():
    return render_template('manager/manager-main.html')

@app.route('/manager-login', methods=['GET', 'POST'], endpoint='managerLoginPage')
def managerLoginPage():
    form = AdminLoginForm()
    if form.validate_on_submit():
        flash('Manager Login Successful!', 'success')
        return redirect(url_for('managerMainPage'))
    return render_template('manager/manager-login.html', form=form)

@app.route('/manager-forgot-password', endpoint='managerForgotPasswordPage')
def managerForgotPasswordPage():
    return render_template('manager/manager-forgot-password.html')


@app.route('/admin-main', endpoint='adminMainPage')
def adminMainPage():
    return render_template('admin/admin-main.html')

@app.route('/admin-login', methods=['GET', 'POST'], endpoint='adminLoginPage')
def adminLoginPage():
    form = AdminLoginForm()
    if form.validate_on_submit():
        flash('Admin Login Successful!', 'success')
        return redirect(url_for('adminMainPage'))  # Correct endpoint for redirection
    return render_template('admin/admin-login.html', form=form)

@app.route('/admin-forgot-password', endpoint='adminForgotPasswordPage')
def adminForgotPasswordPage():
    return render_template('admin/admin-forgot-password.html')

# If you are directly running the application
if __name__ == '__main__':
    app.run(debug=True)
