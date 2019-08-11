from flask import render_template, Blueprint, request, flash, redirect, url_for

from app import db
from app.models import Blog


main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html', title="Home")

@main.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title="About")



@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', title=e, e=e), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html', title=e), 500


@main.app_errorhandler(403)
def forbidden(e):
    return render_template('errors/403.html', title=e, e=e), 403
