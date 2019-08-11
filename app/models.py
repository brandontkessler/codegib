from flask import current_app
from app import db, login_manager, bcrypt
from flask_login import UserMixin
import datetime as dt


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128), nullable=False)
    confirmed = db.Column(db.Boolean, default=False)
    blog_priv = db.Column(db.Boolean, default=False)
    admin_priv = db.Column(db.Boolean, default=False)
    blogs = db.relationship('Blog', backref='blog_author', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt\
            .generate_password_hash(password)\
            .decode('utf-8')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"User('{self.email}')"


class Blog(db.Model):
    __tablename__ = 'blog'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    date = db.Column(db.DateTime, default=dt.datetime.utcnow())
    author = db.Column(db.String(50), default="Brandon Kessler")
    _content = db.Column(db.Text, nullable=False)
    headline = db.Column(db.String(150), nullable=False, default="Please select a headline")
    _tags = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    @property
    def user(self):
        return self.user_id

    @property
    def tags(self):
        tags = [tag.capitalize() for tag in self._tags.split(';')]
        return ", ".join(tags)

    @tags.setter
    def tags(self, tags):
        split_tags = [tag.strip() for tag in tags.split(",")]
        self._tags = "all"
        for tag in split_tags:
            self._tags += f";{tag.lower()}"

    def tag_adder(self, new_tag):
        if new_tag not in self._tags:
            self._tags += f";{new_tag.lower()}"

    def tag_remover(self, tags):
        split_tags = [tag for tag in self._tags.split(';')]
        split_tags.remove("all")
        for tag_to_remove in split_tags:
            split_tags.remove(tag_to_remove)

        for tag in split_tags:
            self._tags = "all;" + f";{tag}"


    def __repr__(self):
        return f"Blog about {self.title} with tags: {self.tags}"


class Carousel(db.Model):
    __tablename__ = 'carousel'

    id = db.Column(db.Integer, primary_key=True)
    img_path = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    source = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"A carousel, featured article titled: {self.title}"


###################
## API DATA SETS

class NBA_Player_Stats(db.Model):
    __tablename__ = 'nba_player_stats'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    game_type = db.Column(db.String(128))
    team = db.Column(db.String(128))
    opponent = db.Column(db.String(50))
    home = db.Column(db.Boolean)
    name = db.Column(db.String(64))
    minutes = db.Column(db.Integer)
    points = db.Column(db.Integer)
    rebounds = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    steals = db.Column(db.Integer)
    blocks = db.Column(db.Integer)
    fouls = db.Column(db.Integer)
    turnovers = db.Column(db.Integer)
    o_rebounds = db.Column(db.Integer)
    d_rebounds = db.Column(db.Integer)
    fg_made = db.Column(db.Integer)
    fg_att = db.Column(db.Integer)
    ft_made = db.Column(db.Integer)
    ft_att = db.Column(db.Integer)
    three_pts_made = db.Column(db.Integer)
    three_pts_att = db.Column(db.Integer)
    plus_minus = db.Column(db.Integer)

    def __repr__(self):
        return f"NBA_Player(player: {self.name}, opponent: {self.opponent}, home: {self.home})"


class NBA_Player_Info(db.Model):
    __tablename__ = 'nba_player_info'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    position = db.Column(db.String(50))
    age = db.Column(db.String(50))
    height = db.Column(db.String(50))
    weight = db.Column(db.String(50))
    college = db.Column(db.String(50))
    salary = db.Column(db.String(50))

    def __repr__(self):
        return f"NBA_Player_Info(player: {self.name}, age: {self.age}, salary: {self.salary})"
