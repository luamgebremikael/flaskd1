from app import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True)
    Firstname= db.Column(db.String(64),unique=True)
    Lastnamename = db.Column(db.String(64),unique=True)
    email = db.Column(db.String(120),unique=True)
    password = db.Column(db.String(120),unique=True)
    
    

class car(db.Model):   
    id = db.Column(db.Integer,primary_key=True)
    make = db.Column(db.String(64),unique=True)
    model = db.Column(db.String(64),unique=True)
    year =  db.Column(db.Integer,primary_key=True)
    color = db.Column(db.String(64),unique=True)
    price = db.Column(db.Integer,primary_key=True)
    datecreated = db.Column(db.Integer,primary_key=True)
    User_id = db.Column(db.Integer,primary_key=True)

    def __repr__(self):
        return f'User:{self.username}'




