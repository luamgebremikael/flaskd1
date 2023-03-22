from flask import render_template, flash, redirect
from app import app, db
from app.forms import RegisterForm, LoginInForm, BlogForm, CarForm
from app.models import User, Car, Blog
from flask_login import current_user, login_user, logout_user, login_required

@app.route('/', methods=['GET', 'POST'])
def car():
    form=CarForm()
    if form.validate_on_submit():
        year = form.year.data
        make = form.make.data
        model = form.model.data
        color = form.color.data
        price = form.price.data
        description = form.description.data
        c = Car(year=year, make=make, model=model,color=color,price=price,description=description)
        c.commit()
        flash(f'Car information sent!')
    return render_template('index.html.jinja', car_form=form, title='Home')

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form =RegisterForm()
    if form.validate_on_submit():
        username=form.username.data
        email= form.email.data
        password=form.password.data
        first_name= form.first_name.data
        last_name= form.last_name.data
        u = User(username=username, email=email, password=password, first_name=first_name,last_name=last_name)
        user_match = User.query.filter_by(username=username).first()
        email_match = User.query.filter_by(email=email).first()
        if user_match:
            flash(f'Username {username} already exists, try again! ')
            return redirect('/register')
        elif email_match:
            flash(f'Email {email} already exists, try again!')
            return redirect('/register')
        else:
            u.commit()
            flash(f'Request to register {username} successful!')
            return redirect('/')
    return render_template('register.jinja', form=form)

@app.route('/login', methods=['GET','POST'])
def log_in():
    form=LoginInForm()
    if form.validate_on_submit():
        username= form.username.data
        password= form.password.data
        user_match= User.query.filter_by(username=username).first()
        if not user_match or user_match.password != password:
            flash(f'Username or Passowrd does not work, try again!')
            return redirect('/login')
        flash(f'{username} successfully signed in!')
        login_user(user_match)
        return redirect('/')
    return render_template('login.jinja', log_in_form=form)

@app.route('/blog', methods=['GET','POST'])
@login_required
def blog():
    form=BlogForm()
    if form.validate_on_submit():
        blogblock=form.blogblock.data
        b=Blog(blogblock=blogblock) 
        b.commit()
        flash(f'Successfully sent a Blog!')
    return render_template('blog.jinja', blog_form=form)


@app.route('/signout')
@login_required
def sign_out():
    logout_user()
    return redirect('/')

@app.route('/user/<username>')
def user(username):
    user_match = User.query.filter_by(username=username).first()
    if not user_match:
        return redirect ('/')
    posts = user_match.posts
    return render_template('user.jinja', user=user_match, posts=posts)