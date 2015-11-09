from flask import flash, redirect, render_template, \
    url_for, Blueprint, session, request, jsonify
from app import db
from app.models import Post, User


blog_blueprint = Blueprint("blog", __name__, static_folder=None,
                           static_url_path=None, template_folder='templates',
                           url_prefix=None, subdomain=None, url_defaults=None)
# Add Route by stating
# @nameofblueprint_blueprint.route

# To access the Database
# User.query.filter_by(username=request.form['username']).first()


@blog_blueprint.route('/', methods=['GET'])
def index():
    user = User.query.filter_by(username='Kyle').first()
    return jsonify(firstName=user.username, lastName=user.lastName)


@blog_blueprint.route('/blog', methods=['GET'])
def test_blog():
    post = Post.query.first()
    return jsonify(post=post.author.username, content=post.post_data)
