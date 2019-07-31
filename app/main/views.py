from flask import render_template, Blueprint, request
from flask_login import login_required
from app.decorators import check_confirmed, check_admin
from app.models import Blog

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    # Query Params
    page = request.args.get('page', 1, type=int)
    tag_filter = request.args.get('tag_filter', 'all', type=str)

    # Query all blogs
    all_blogs = Blog.query.order_by(Blog.date.desc())

    # Filter by query params
    blogs = all_blogs.filter(Blog._tags.ilike(f"%{tag_filter}%"))\
                    .paginate(page=page, per_page=6)

    # Identify and sort tags by total count
    all_tag_list = [tag.capitalize() for blog in all_blogs.all() for tag in blog.tags]
    all_tags = {tag: all_tag_list.count(tag) for tag in all_tag_list}
    sorted_tags = sorted(all_tags, key=lambda k: all_tags[k], reverse=True)


    return render_template('index.html', title="Home Blog", blogs=blogs,
                            sorted_tags=sorted_tags, tag_filter=tag_filter)

@main.route('/blog/<blog_title>', methods=['GET'])
def blog(blog_title):
    # Query blog
    blog = Blog.query.filter_by(title=blog_title).get_or_404()

    return render_template('blogs/blog_post.html', title="Blog Post", blog=blog,
                            )

@main.route("/secret")
@login_required
@check_confirmed
@check_admin
def secret():
    return "SECRET PAGE"



@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', title=e, e=e), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html', title=e), 500


@main.app_errorhandler(403)
def forbidden(e):
    return render_template('errors/403.html', title=e), 403
