from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Member(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),unique=True)
    password = db.Column(db.String(30))
    email = db.Column(db.String(50))
    join_date = db.Column(db.DateTime)
#one to many relationship code
    orders = db.relationship('Order',backref='member',lazy='dynamic')
#Many to many relationship code
    courses = db.relationship('Course',secondary='user_courses',backref='member',lazy='dynamic')


    def __init__(self,username,password,email,join_date):

        self.username = username
        self.password = password
        self.email = email
        self.join_date = join_date

    def __repr__(self):

        return f"Member: {self.username}"
#One to many relationship
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    member_id = db.Column(db.Integer,db.ForeignKey('member.id'))

#Many to many relationship
class Course(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))

db.Table('user_courses',
        db.Column('member_id',db.Integer,db.ForeignKey('member.id')),
        db.Column('course_id',db.Integer,db.ForeignKey('course.id'))
        )

if __name__ == "__main__":
    app.run()
