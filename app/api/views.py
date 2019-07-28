import json

from flask import (render_template, url_for, redirect, jsonify,
    request, Blueprint)

from app import db
from app.models import NBA_Player_Stats

api = Blueprint('api', __name__)


@api.route("/", methods=['GET'])
def api_index():
    return render_template('api/api_index.html', title="API Index")


@api.route("/usage/nba", methods=['GET'])
def usage_nba():

    players_query = db.session.query(NBA_Player_Stats.name)\
        .distinct().order_by(NBA_Player_Stats.name)

    players_dict = [player.name for player in players_query]
    players = json.dumps(players_dict)

    return render_template('api/usage_nba.html', title="API Usage",
        players=players)


@api.route("/nba_players", methods=['GET'])
def nba_players():

    players_query = db.session.query(NBA_Player_Stats.name)\
        .distinct().order_by(NBA_Player_Stats.name)

    players = [player.name for player in players_query]

    return jsonify(players)


@api.route("/nba_stats", methods=['GET'])
def nba_stats_api():

    player_name = request.args['player']

    player_stats = NBA_Player_Stats.query.filter_by(name=player_name).all()

    player_object = {
        player_name: []
    }

    for row in player_stats:
        game_info = {
            'game_type': row.game_type,
            'team': row.team,
            'opponent': row.opponent,
            'home': row.home
        }

        game_stats = {
            'minutes': row.minutes,
            'points': row.points,
            'rebounds': row.rebounds,
            'assists': row.assists,
            'steals': row.steals,
            'blocks': row.blocks,
            'fouls': row.fouls,
            'turnovers': row.turnovers,
            'o_rebounds': row.o_rebounds,
            'd_rebounds': row.d_rebounds,
            'fg_made': row.fg_made,
            'fg_att': row.fg_att,
            'ft_made': row.ft_made,
            'ft_att': row.ft_att,
            'three_pts_made': row.three_pts_made,
            'three_pts_att': row.three_pts_att,
            'plus_minus': row.plus_minus
        }

        stats_object = {
            str(row.date): {
                'game_info': game_info,
                'game_stats': game_stats
            }
        }

        player_object[player_name].append(stats_object)



    return jsonify(player_object)
