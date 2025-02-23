import json
import requests
import sys

from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
from psycopg2 import sql


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages


def get_db_connection():
    return psycopg2.connect(
        dbname="your_db_name",
        user="your_db_user",
        password="your_db_password",
        host="your_db_host",
        port="your_db_port"
    )
    
    
# employee Routes

# employee Main
@app.route('/employee-main')
def employeeMainPage():
    return render_template('employee/employee-main.html')

# employee Login
@app.route('/employee-login', endpoint='employeeLoginPage')
def employeeLoginPage():
    return render_template('employee/employee-login.html')

# employee Register
@app.route('/employee-register', endpoint='employeeRegisterPage')
def employeeRegisterPage():
    return render_template('employee/employee-register.html')

# employee Forgot Password
@app.route('/employee-forgot-password', endpoint='employeeForgotPasswordPage')
def employeeForgotPasswordPage():
    return render_template('employee/employee-forgot-password.html')

# employee supplies requests
@app.route('/employee-supplies-requests', endpoint='employeeSuppliesRequestsPage')
def employeeSuppliesRequestsPage():
    return render_template('employee/employee-supplies-requests.html')

# employee vacation requests
@app.route('/employee-vacation-requests', endpoint='employeeVacationRequestsPage')
def employeeVactionRequestsPage():
    return render_template('employee/employee-vacation-requests.html')

# employee submit vacation request
@app.route('/submit-vacation-request', methods=['GET', 'POST'], endpoint='submitVacationRequest')
def submitVacationRequest():
    if request.method == 'POST':
        employee_id = 1  # Replace with actual logged-in user ID
        trip_type = request.form['trip_type']
        leave_date = request.form['leave_date']
        return_date = request.form['return_date']
        cost = request.form['cost'] if request.form['cost'] else None
        reason = request.form['reason']

        try:
            conn = get_db_connection()
            cur = conn.cursor()

            cur.execute("SELECT employee_submit_vacation_request(%s, %s, %s, %s, %s, %s)",
                        (employee_id, trip_type, leave_date, return_date, cost, reason))

            conn.commit()
            cur.close()
            conn.close()

            flash('Vacation request submitted successfully!', 'success')
            return redirect(url_for('submitVacationRequest'))

        except Exception as e:
            flash(f'Error submitting vacation request: {e}', 'danger')

    # Fetch vacation requests for display
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM vacation_requests ORDER BY leave_date DESC")
        vacation_requests = cur.fetchall()
        cur.close()
        conn.close()
    except Exception as e:
        flash(f'Error fetching vacation requests: {e}', 'danger')
        vacation_requests = []

    return render_template('employee/employee-vacation-requests.html', vacation_requests=vacation_requests)
# manager Routes

# manager Main
@app.route('/manager-main')
def managerMainPage():
    return render_template('manager/manager-main.html')

# manager Login
@app.route('/manager-login', endpoint='managerLoginPage')
def managerLoginPage():
    return render_template('manager/manager-login.html')

# manager Register
@app.route('/manager-register', endpoint='managerRegisterPage')
def managerRegisterPage():
    return render_template('manager/manager-register.html')

# manager Forgot Password
@app.route('/manager-forgot-password', endpoint='managerForgotPasswordPage')
def managerForgotPasswordPage():
    return render_template('manager/manager-forgot-password.html')

# manager employees
@app.route('/manager-employees', endpoint='managerEmployeesPage')
def managerEmployeesPage():
    return render_template('manager/manager-employees.html')

# manager vacation requests
@app.route('/manager-vacation-requests', endpoint='managerVacationRequestsPage')
def managerVacationRequestsPage():
    return render_template('manager/manager-vacation-requests.html')

# manager supplies requests
@app.route('/manager-supplies-requests', endpoint='managerSuppliesRequestsPage')
def managerSuppliesRequestsPage():
    return render_template('manager/manager-supplies-requests.html')

# Admin Routes

# admin Main 
@app.route('/admin-main', endpoint='adminMainPage')
def adminMainPage():
    return render_template('admin/admin-main.html')

# admin Login
@app.route('/admin-login', endpoint='adminLoginPage')
def adminLoginPage():
    return render_template('admin/admin-login.html')

# admin Register
@app.route('/admin-register', endpoint='adminRegisterPage')
def adminRegisterPage():
    return render_template('admin/admin-register.html')

# admin Forgot Password
@app.route('/admin-forgot-password', endpoint='adminForgotPasswordPage')
def adminForgotPasswordPage():
    return render_template('admin/admin-forgot-password.html')
 
# admin employees
@app.route('/admin-employees', endpoint='adminEmployees')
def adminEmployees():
    return render_template('admin/admin-employees.html')

# admin managers
@app.route('/admin-managers', endpoint='adminManagers')
def adminManagers():
    return render_template('admin/admin-managers.html')

# admin reports
@app.route('/admin-reports', endpoint='adminReports')
def adminReports():
    return render_template('admin/admin-reports.html')

# admin requests
@app.route('/admin-requests', endpoint='adminRequests')
def adminRequests():
    return render_template('admin/admin-requests.html')
