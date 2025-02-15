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
    
# Student Routes
@app.route('/student-main')
def studentMainPage():
    return render_template('student/student-main.html')

@app.route('/student-login', endpoint='studentLoginPage')
def studentLoginPage():
    return render_template('student/student-login.html')

@app.route('/student-register', endpoint='studentRegisterPage')
def studentRegisterPage():
    return render_template('student/student-register.html')

@app.route('/student-forgot-password', endpoint='studentForgotPasswordPage')
def studentForgotPasswordPage():
    return render_template('student/student-forgot-password.html')

# Teacher Routes
@app.route('/teacher-main')
def teacherMainPage():
    return render_template('teacher/teacher-main.html')

@app.route('/teacher-login', endpoint='teacherLoginPage')
def teacherLoginPage():
    return render_template('teacher/teacher-login.html')

@app.route('/teacher-register', endpoint='teacherRegisterPage')
def teacherRegisterPage():
    return render_template('teacher/teacher-register.html')

@app.route('/teacher-forgot-password', endpoint='teacherForgotPasswordPage')
def teacherForgotPasswordPage():
    return render_template('teacher/teacher-forgot-password.html')

# Admin Routes
@app.route('/admin-main')
def adminMainPage():
    return render_template('admin/admin-main.html')

@app.route('/admin-login', endpoint='adminLoginPage')
def adminLoginPage():
    return render_template('admin/admin-login.html')

@app.route('/admin-register', endpoint='adminRegisterPage')
def adminRegisterPage():
    return render_template('admin/admin-register.html')

@app.route('/admin-forgot-password', endpoint='adminForgotPasswordPage')
def adminForgotPasswordPage():
    return render_template('admin/admin-forgot-password.html')
 
