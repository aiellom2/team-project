from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import AdminLoginForm
from app import db
from app.models import User
import sys


# Employee Routes


@app.route('/admin-main')
def adminMain():
    return render_template('admin/admin-main.html')

@app.route('/admin-login', methods=['GET', 'POST'])
def adminLogin():
    form = AdminLoginForm()
    if form.validate_on_submit():
        flash('DB CHECK LOGIN INFO HERE')
        return redirect(url_for('admin-main.html'))
    return render_template('admin/admin-login.html', form=form)

@app.route('/admin-forgot-password')
def adminForgotPassword():
    return render_template('admin/admin-forgot-password.html')

# If you are directly running the application
if __name__ == '__main__':
    app.run(debug=True)
