from app import db, login
from datetime import datetime
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id= db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(64), unique=True, nullable=True)
    email= db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(120), nullable=True)
    first_name= db.Column(db.String(64))
    last_name= db.Column(db.String(64))
    blogs= db.relationship('Blog', backref='narrator', lazy='dynamic')
    posts= db.relationship('Car', backref='author', lazy='dynamic')


    def __repr__(self):
        return f'<User: {self.username}>'
    
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    
class Blog(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    blogblock = db.Column(db.String(250))
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Blogs: {self.blogblock}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
    
    

class Car(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    year= db.Column(db.String(64), nullable=True)
    make= db.Column(db.String(64), nullable=True)
    model = db.Column(db.String(64), nullable=True)
    color= db.Column(db.String(64))
    price= db.Column(db.String(64), nullable=True)
    description= db.Column(db.String(250))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Info: {self.year}, {self.make}, {self.model}, {self.color}, {self.price}, {self.description}!>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
    


