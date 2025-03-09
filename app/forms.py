from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email


class AdminLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Admin Login')

class ManagerLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Manager Login')

class EmployeeLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Employee Login')

class RequestTypeForm(FlaskForm):
    name = StringField('Request Type Name', validators=[DataRequired()])
    submit = SubmitField('Add Request Type')

class AddManagerForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Add Manager')

class AddEmployeeForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Add Employee')

class OfficeSupplyForm(FlaskForm):
    name = StringField('Office Supply Name', validators=[DataRequired()])
    price = StringField('Office Supply Price Per Unit', validators=[DataRequired()])
    stock = StringField('Office Supply Stock / Quantity', validators=[DataRequired()])
    submit = SubmitField('Add Office Supply')