from app import db,login
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,nullable=True)
    Firstname= db.Column(db.String(64),unique=True,nullable=True)
    Lastname = db.Column(db.String(64),unique=True,nullable=True)
    email = db.Column(db.String(120),unique=True,nullable=True)
    password = db.Column(db.String(120),unique=True,nullable=True)
    cars = db.relationship('car',backref='author',lazy='dynamic')
    

    def __str__(self):
        return f'User:{self.username}|{self.Firstname}|{self.Lastname}|{self.email}|{self.password}'
    def commit(self):
        db.session.add(self)
        db.session.commit()
    

class car(db.Model):   
    id = db.Column(db.Integer,primary_key=True)
    make = db.Column(db.String(64),unique=True)
    model = db.Column(db.String(64),unique=True)
    year =  db.Column(db.Integer,primary_key=True)
    color = db.Column(db.String(64),unique=True)
    price = db.Column(db.Integer,primary_key=True)
    datecreated = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __str__(self):
        return f'car:{self.make}|{self.model}|{self.year}|{self.color}'
    def __int__(self):
        return f'car:{self.datecreated}|{self.User_id}'



