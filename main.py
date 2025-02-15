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
# Student Main
@app.route('/student-main')
def studentMainPage():
    return render_template('student/student-main.html')

# Student Login
@app.route('/student-login', endpoint='studentLoginPage')
def studentLoginPage():
    return render_template('student/student-login.html')

# Student Register
@app.route('/student-register', endpoint='studentRegisterPage')
def studentRegisterPage():
    return render_template('student/student-register.html')

# Student Forgot Password
@app.route('/student-forgot-password', endpoint='studentForgotPasswordPage')
def studentForgotPasswordPage():
    return render_template('student/student-forgot-password.html')

# Student Objectives
@app.route('/student-objectives', endpoint='studentObjectivesPage')
def studentObjectivesPage():
    return render_template('student/student-objectives.html')

# Student Users
@app.route('/student-users', endpoint='studentUsersPage')
def studentUsersPage():
    return render_template('student/student-users.html')

# Student Needs
@app.route('/student-needs', endpoint='studentNeedsPage')
def studentNeedsPage():
    return render_template('student/student-needs.html')

# Student Stories
@app.route('/student-stories', endpoint='studentStoriesPage')
def studentStoriesPage():
    return render_template('student/student-stories.html')

# Student Features
@app.route('/student-features', endpoint='studentFeaturesPage')
def studentFeaturesPage():
    return render_template('student/student-features.html')

# Student Diagrams
@app.route('/student-diagrams', endpoint='studentDiagramsPage')
def studentDiagramsPage():
    return render_template('student/student-diagrams.html')

# Teacher Routes
# Teacher Main
@app.route('/teacher-main')
def teacherMainPage():
    return render_template('teacher/teacher-main.html')

# Teacher Login
@app.route('/teacher-login', endpoint='teacherLoginPage')
def teacherLoginPage():
    return render_template('teacher/teacher-login.html')

# Teacher Register
@app.route('/teacher-register', endpoint='teacherRegisterPage')
def teacherRegisterPage():
    return render_template('teacher/teacher-register.html')

# Teacher Forgot Password
@app.route('/teacher-forgot-password', endpoint='teacherForgotPasswordPage')
def teacherForgotPasswordPage():
    return render_template('teacher/teacher-forgot-password.html')

# Teacher Objectives
@app.route('/teacher-objectives', endpoint='teacherObjectivesPage')
def teacherObjectivesPage():
    return render_template('teacher/teacher-objectives.html')

# Teacher Users
@app.route('/teacher-users', endpoint='teacherUsersPage')
def teacherUsersPage():
    return render_template('teacher/teacher-users.html')

# Teacher Needs
@app.route('/teacher-needs', endpoint='teacherNeedsPage')
def teacherNeedsPage():
    return render_template('teacher/teacher-needs.html')

# Teacher Stories
@app.route('/teacher-stories', endpoint='teacherStoriesPage')
def teacherStoriesPage():
    return render_template('teacher/teacher-stories.html')

# Teacher Features
@app.route('/teacher-features', endpoint='teacherFeaturesPage')
def teacherFeaturesPage():
    return render_template('teacher/teacher-features.html')

# Teacher Diagrams
@app.route('/teacher-diagrams', endpoint='teacherDiagramsPage')
def teacherDiagramsPage():
    return render_template('teacher/teacher-diagrams.html')


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
 
