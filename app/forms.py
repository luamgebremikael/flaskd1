from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo

class signupForms(FlaskForm):
    username= StringField('Username',validators=[DataRequired()])
    email= StringField('email',validators=[DataRequired()])
    password= PasswordField('Password',validators=[DataRequired()])
    Firstname=StringField('Firstname',validators=[DataRequired()])
    Lastname=StringField('Lastname',validators=[DataRequired()])
    confirm_password= PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('signup')

class LoginForms(FlaskForm):
    email= StringField('email',validators=[DataRequired()]) 
    password= PasswordField('Password',validators=[DataRequired()])  
    submit=SubmitField('Login')

class carForms(FlaskForm):
    make= StringField('make',validators=[DataRequired()])
    model= StringField('model',validators=[DataRequired()])
    year= PasswordField('year',validators=[DataRequired()])
    color=StringField('color',validators=[DataRequired()])
    price= PasswordField('price',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('signup')