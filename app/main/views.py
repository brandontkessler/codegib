from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask_login import login_required, current_user

from app import db
from app.decorators import check_confirmed, check_admin, check_blogger
from app.models import Blog
from app.main.forms import BlogPostForm


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
def read_blog(blog_title):
    # Query blog
    blog = Blog.query.filter_by(title=blog_title).first_or_404()

    return render_template('blogs/read_blog.html', title="Blog Post", blog=blog)


@main.route('/post_blog', methods=['GET', 'POST'])
@login_required
@check_confirmed
@check_blogger
def post_blog():
    form = BlogPostForm()

    if form.validate_on_submit(): # For valid post request
        content = [
            par.strip() for par in form.content.data.strip()\
            .replace("\r", "").split("\n") if par != ""
        ]
        content = ';'.join(content)

        blog = Blog(
            title=form.title.data.strip(),
            author=form.author.data.strip() or 'Brandon Kessler',
            _content=content,
            headline=form.headline.data.strip(),
            tags=tags,
            user_id=current_user.id
        )

        db.session.add(blog)
        db.session.commit()

        flash('Your blog has been submitted.', 'success')
        return redirect(url_for('main.index'))

    # Parse all the titles from blogs (use this to check that title is unique)
    blogs = [blog[0].lower() for blog in Blog.query.with_entities(Blog.title)]

    return render_template('blogs/post_blog.html', title="Post a Blog", form=form, blogs=blogs)


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
    return render_template('errors/403.html', title=e, e=e), 403
