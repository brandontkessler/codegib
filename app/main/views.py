from flask import render_template, Blueprint, request, flash, redirect, url_for

from app import db
from app.models import Blog, Carousel


main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    # Carousel items
    carousel_items = Carousel.query.all()

    # Top 3 blogs
    blog_title_1 = 'This is the first title to This Blog'
    blog_title_2 = '5 Blogasdf'
    blog_title_3 = 'This is my first blog'

    blog1 = Blog.query.filter_by(title=blog_title_1).first_or_404()
    blog2 = Blog.query.filter_by(title=blog_title_2).first_or_404()
    blog3 = Blog.query.filter_by(title=blog_title_3).first_or_404()

    top_3_blogs = blog1, blog2, blog3

    return render_template('index.html', title="Home",
                           carousel_items=carousel_items,
                           top_3_blogs=top_3_blogs)


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
