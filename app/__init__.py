# import the Flask class from the flask module
import os
from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
# create the application object
app = Flask(__name__)

# Configuration
app.config.from_object(os.environ['APP_SETTINGS'])
# Data base
db = SQLAlchemy(app)

# Attach blue-prints here with app.register_blueprint
# Remeber to add __init__.py to sub blueprints

# Process before requests with
# @app.before_request
# use decorators to link the function to a url


@app.route("/")
@app.route("/hello")
# define the view using a function, which returns a string
def hello_world():
    return "Hello, World!"


# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query


# dynamic route with explicit status codes
@app.route("/name/<name>")
def index(name):
    obj = {name: name.lower()}
    return jsonify(obj)
