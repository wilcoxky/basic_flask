from app import db
from app.models import User, Post

db.drop_all()
db.create_all()

user = User('Kyle', 'email', 'firstName', 'lastName', 'password')
db.session.add(user)
db.session.commit()

post = {'title': "Kyle\'s test blog post",
        'content': "This is my random text from the post I hope its formatted correctly here"}

post = Post(1, post)
db.session.add(post)
db.session.commit()
