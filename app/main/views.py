from flask import render_template, Blueprint, request, flash, redirect, url_for, send_from_directory

from app import db
from app.models import Blog, Carousel


main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    # Carousel items
    carousel_items = Carousel.query.all()

    # Top 3 blogs
    blog1 = {
        'title': 'AAARRR! What are Pirate Metrics?',
        'url': 'https://www.activecampaign.com/blog/aaarrr-what-are-pirate-metrics',
        'author': 'Jordan Skole',
        'source': 'ActiveCampaign',
        'feature_img_path': 'img/carousel/pirate_metrics.png'
    }

    blog2 = {
        'title': 'Clustering: Why to Use it',
        'url': 'https://towardsdatascience.com/clustering-why-to-use-it-16d8e2fbafe',
        'author': 'Robert Miller',
        'source': 'Medium',
        'feature_img_path': 'img/carousel/clustering.png'
    }

    blog3 = {
        'title': 'Supervised vs. Unsupervised Learning',
        'url': 'https://towardsdatascience.com/supervised-vs-unsupervised-learning-14f68e32ea8d',
        'author': 'Devin Soni',
        'source': 'Medium',
        'feature_img_path': 'img/carousel/supervised_vs_unsupervised.gif'
    }


    top_3_blogs = blog1, blog2, blog3

    return render_template('index.html', title="Home",
                           carousel_items=carousel_items,
                           top_3_blogs=top_3_blogs)


@main.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title="About")


@main.route('/robots.txt')
@main.route('/sitemap.xml')
def static_from_root():
    return send_from_directory('static', request.path[1:])


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', title=e, e=e), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html', title=e), 500


@main.app_errorhandler(403)
def forbidden(e):
    return render_template('errors/403.html', title=e, e=e), 403
