from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email

class RegisterForm(FlaskForm):
    username = StringField('Username', validators= [DataRequired()])
    email = StringField('Email', validators =[DataRequired(), Email()])
    password = PasswordField('Password', validators= [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators= [DataRequired(), EqualTo('password', message='Passwords must match!')])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me= BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class BlogForm(FlaskForm):
    blogblock = TextAreaField('', validators=[DataRequired()])
    submit = SubmitField('Submit Post')

class CarForm(FlaskForm):
    year = StringField('Year', validators=[DataRequired()])
    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Send Info')
