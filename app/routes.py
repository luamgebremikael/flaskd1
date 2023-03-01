from flask import render_template
from app import app 


@app.route('/')
def rest():
    resturants={
        'employers':('jerry','Abiel'),
        'Tabels':['Tabel 1','Tabel 2','Tabel 3','Tabel 4','Tabel 5']

    }
    return render_template('rest.html.jinja', cafe=resturants, title='Home')

@app.route('/Home')
def Home():
    return render_template('Home.jinja') 
@app.route('/Login')   
def Login():
    return render_template('Login.jinja')  
@app.route('/Register')  
def Register():

    
    return render_template('Register.jinja')
@app.route('/About')    
def About():
    return render_template('About.jinja') 
@app.route('/Blog')   
def Blog():
    return render_template('Blog.jinja')    
