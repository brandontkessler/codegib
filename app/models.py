from flask import current_app
from app import db, login_manager
from flask_login import UserMixin
import datetime as dt


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128), nullable=False)
    confirmed = db.Column(db.Boolean, default=False)
    blog_priv = db.Column(db.Boolean, default=False)
    admin_priv = db.Column(db.Boolean, default=False)
    blogs = db.relationship('Blog', backref='blog_author', lazy='dynamic')

    def __repr__(self):
        return f"User('{self.email}')"


class Blog(db.Model):
    __tablename__ = 'blog'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    date = db.Column(db.DateTime, default=dt.datetime.utcnow())
    author = db.Column(db.String(50), default="Brandon Kessler")
    content = db.Column(db.Text, nullable=False)
    _tags = db.Column(db.String(128), default="all")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    @property
    def tags(self):
        return [tag for tag in self._tags.split(';')]

    @tags.setter
    def tags(self, values):
        if isinstance(values, list):
            for tag in values:
                self._tags += f";{tag}"
        else:
            print("ERROR THAT IS NOT A LIST")

    def tag_adder(self, values):
        if isinstance(values, list):
            for tag in values:
                self._tags += f";{tag}"
        else:
            print("ERROR THAT IS NOT A LIST")

    def tag_remover(self, values):
        if isinstance(values, list):
            tags = [tag for tag in self._tags.split(';')]
            tags.remove("all")
            for tag_to_remove in values:
                tags.remove(tag_to_remove)

            self._tags = "all"
            for tag in tags:
                self._tags += f";{tag}"
        else:
            print("ERROR THAT IS NOT A LIST")

    def __repr__(self):
        return f"Blog about {self.title} with tags: {self.tags}"




###################
## API DATA SETS

class NBA_Player_Stats(db.Model):
    __tablename__ = 'nba_player_stats'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    game_type = db.Column(db.String(10))
    team = db.Column(db.String(10))
    opponent = db.Column(db.String(3))
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
    position = db.Column(db.String(10))
    age = db.Column(db.Integer)
    height = db.Column(db.String(10))
    weight = db.Column(db.String(10))
    college = db.Column(db.String(10))
    salary = db.Column(db.String(10))

    def __repr__(self):
        return f"NBA_Player_Info(player: {self.name}, age: {self.age}, salary: {self.salary})"
