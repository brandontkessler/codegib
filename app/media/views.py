from flask import render_template, Blueprint, request, flash, redirect, url_for, send_file
from flask_login import login_required, current_user

from app import db
from app.decorators import check_confirmed, check_admin, check_blogger
from app.models import Blog
from app.media.forms import BlogPostForm

media = Blueprint('media', __name__)


@media.route('/', methods=['GET', 'POST'])
def media_index():
    # Query Params
    tag_filter = request.args.get('tag_filter', 'all', type=str)

    # Query all blogs
    all_blogs = Blog.query.order_by(Blog.date.desc())

    # Filter by query params
    blogs = all_blogs.filter(Blog._tags.ilike(f"%{tag_filter}%")).all()

    # Identify and sort tags by total count
    all_tag_list = [tag.strip() for blog in all_blogs.all() for tag in blog.tags.strip().split(",")]
    all_tags = {tag: all_tag_list.count(tag) for tag in all_tag_list}
    sorted_tags = sorted(all_tags, key=lambda k: all_tags[k], reverse=True)

    return render_template('media/media.html', title="Media Home", blogs=blogs,
                            sorted_tags=sorted_tags, tag_filter=tag_filter)

@media.route('/blog/<blog_title>', methods=['GET'])
def read_blog(blog_title):
    # Query blog
    blog = Blog.query.filter_by(title=blog_title).first_or_404()

    return render_template('media/blogs/read_blog.html', title="Blog Post", blog=blog)


@media.route('/post_blog', methods=['GET', 'POST'])
@login_required
@check_confirmed
@check_blogger
def post_blog():
    form = BlogPostForm()

    if form.validate_on_submit(): # For valid post request
        blog = Blog(
            title=form.title.data.strip(),
            author=form.author.data.strip() or 'Brandon Kessler',
            feature_img_path=form.feature_img_path.data.strip(),
            _content=form.content.data,
            headline=form.headline.data.strip(),
            tags=form.tags.data,
            user_id=current_user.id
        )

        db.session.add(blog)
        db.session.commit()

        flash('Your blog has been submitted.', 'success')
        return redirect(url_for('media.media_index'))

    # Parse all the titles from blogs (use this to check that title is unique)
    blogs = [blog[0].lower() for blog in Blog.query.with_entities(Blog.title)]

    return render_template('media/blogs/post_blog.html', title="Post a Blog", form=form, blogs=blogs)


@media.route('/blog/<blog_title>/edit', methods=['GET', 'POST'])
@login_required
@check_confirmed
@check_blogger
def edit_blog(blog_title):
    form = BlogPostForm()
    blog = Blog.query.filter_by(title=blog_title).first_or_404()

    if form.validate_on_submit(): # For valid post request
        blog.title=form.title.data.strip()
        blog.author=form.author.data.strip() or "Brandon Kessler"
        blog.feature_img_path=form.feature_img_path.data.strip()
        blog._content=form.content.data
        blog.headline=form.headline.data.strip()
        blog.tags=form.tags.data

        db.session.commit()

        flash('Your blog has been edited.', 'success')
        return redirect(url_for('media.media_index'))

    return render_template('media/blogs/edit_blog.html', title="Edit a Blog", form=form, blog=blog)


@media.route('/blog/<blog_title>/delete', methods=['GET'])
@login_required
@check_confirmed
@check_blogger
def delete_blog(blog_title):
    blog = Blog.query.filter_by(title=blog_title).first_or_404()

    db.session.delete(blog)
    db.session.commit()

    flash('Your blog has been deleted.', 'success')
    return redirect(url_for('media.media_index'))


@media.route('/get_ltv_csv', methods=['GET'])
def send_sample_file():
    file = 'static/files/data_sample_ltv.csv'
    return send_file(file, as_attachment=True)
