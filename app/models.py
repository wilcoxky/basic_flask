from app import app, db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)

    def __init__(self):
        pass

    def __repr__(self):
        pass


class User(db.Model):
    __tablename__ = "users"
    # Generate Fields that we want for a blog
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    firstName = db.Column(db.String)
    lastName = db.Column(db.String)
    fullName = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, nullable=False)
    posts = relationship('Post', backref='author', cascade='all')
    comments = relationship('Comment', backref='author', cascade='all')

    def __init__(self, username, email, firstName, lastName, password):
        self.username = username
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = firstName + " " + lastName
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username
