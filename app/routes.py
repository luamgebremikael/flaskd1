from flask import render_template,flash,redirect
from app import app
from app.forms import signupForms,LoginForms,carForms



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
    return render_template('Login.jinja',form=form)  
@app.route('/signup',methods=['GET','POST'])  
def signup():
    form=signupForms()
    if form.validate_on_submit():
        flash(f'Request to signup{form.username}sucessfull!')
        
    return render_template('signup.jinja',form=form)
@app.route('/car')    
def car():
    form=carForms()
    return render_template('car.jinja',form=form)
 
