from flask import flash, redirect, render_template, \
    url_for, Blueprint, session, request
from app import db
from app.models import Post


user_blueprint = Blueprint("user", __name__, static_folder=None,
                           static_url_path=None, template_folder='templates',
                           url_prefix=None, subdomain=None, url_defaults=None)
# Add Route by stating
# @nameofblueprint_blueprint.route
