from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from app.models import Blog


class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author (optional)')
    headline = TextAreaField('Headline', validators=[Length(max=200)])
    content = TextAreaField('Content (requires html script; all image srcs must begin with "/static/img/" ... then complete route)', validators=[Length(max=10000)])
    tags = StringField('Tags - Separate tags with commas (food, dogs, python)',
        validators=[Length(max=200)])

    submit = SubmitField('Post Blog')
