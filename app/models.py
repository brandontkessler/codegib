from flask import current_app
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128), nullable=False)
    confirmed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"User('{self.email}')"


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
