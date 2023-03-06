from flask import render_template,flash,redirect
from app import app,db
from app.forms import signupForms,LoginForms,carForms
from app.models import User
from flask_login import login_user


@app.route('/')
def rest():
    carlist={
        'carlist':('Trucks','SUVs'),
        'Brands':['Honda','Nissan','Ford','Jeep','volvo']}
    return render_template('rest.html.jinja', car=carlist, title='Home')

@app.route('/Home')
def Home():
    return render_template('Home.jinja') 
@app.route('/Login',methods=['GET','POST'])   
def Login():
    form=LoginForms()
    if form.validate_on_submit():
        
        password=form.password
        
        flash(f'Request to Login {password} sucessful!')
        #login_user(user_match)
        return redirect('/')
   
    
    return render_template('Login.jinja',form=form)  
@app.route('/signup',methods=['GET','POST'])  
def signup():
    form=signupForms()
    if form.validate_on_submit():
        username=form.username.data
        Firstname=form.Firstname.data
        Lastname=form.Lastname.data
        email=form.email.data
        password=form.password.data
        u = User(username=username,Firstname=Firstname,Lastname=Lastname,email=email,password=password)
        user_match = User.query.filter_by(username=username)
        email_match = User.query.filter_by(email=email)
        if not user_match:
            flash(f'user name {username} already exsists,please try again.')
            return redirect('/signup')
        elif email_match:
            flash(f'email {email} already exsists,please try again.')
            return redirect('/signup')
        else:    
            u.commit()
            flash(f'Request to Signup {username} sucessful!')
            return redirect('/')
        return redirect('/signup')
    return render_template('signup.jinja',form=form)
@app.route('/car')    
def car():
    form=carForms()
    return render_template('car.jinja',form=form)
 
