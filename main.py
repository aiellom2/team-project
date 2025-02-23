import json
import requests
import sys


from flask import Flask, render_template

app = Flask(__name__)

def read_temps():
    city_temps = {}
    cities=['San diego', 'New York', 'Miami', 'Las Vegas', 'Seattle', 'Denver', 'New Haven']
    URL = 'http://api.openweathermap.org/data/2.5/weather'

    for city in cities:
        payload = {'APPID':'d208dfea1c85eb13f4cf52d216ed2f9d', 'q':city}
        response = requests.get(URL,params = payload)

        if response.status_code == 200:
            print('Success!', file = sys.stdout)
        elif response.status_code == 404:
            print ('Failure!', file = sys.stdout)

        response_json = response.json();

        temperature = response_json['main']['temp']
        city_temps[city] = (int((temperature -273)*1.8 + 32))
    return city_temps

@app.route('/temps')
def show_temps():
    city_temps = read_temps()
    return render_template('show_temps.html',template_temps=city_temps)


@app.route('/plot_temps')
def plot_temps():
    city_temps = read_temps()
    cities = list(city_temps.keys())
    temps = list(city_temps.values())
    print(cities, file=sys.stdout)
    print(temps, file=sys.stdout)
    return render_template('plot_temps.html',cities = cities,temps = temps)
    
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
 
