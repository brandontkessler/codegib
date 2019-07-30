import json

from flask import (render_template, url_for, redirect, jsonify,
    request, Blueprint)

from app import db
from app.models import NBA_Player_Stats, NBA_Player_Info

api = Blueprint('api', __name__)


@api.route("/", methods=['GET'])
def api_index():
    return render_template('api/api_index.html',
                            title="API Index")


@api.route("/nba_players", methods=['GET'])
def nba_players():

    players_query = db.session.query(NBA_Player_Stats.name)\
        .distinct().order_by(NBA_Player_Stats.name)

    players = [player.name for player in players_query]

    return jsonify(players)



@api.route("/nba_stats/usage", methods=['GET'])
def nba_stats_api_usage():

    players_query = db.session.query(NBA_Player_Stats.name)\
        .distinct().order_by(NBA_Player_Stats.name)

    players_list = [player.name for player in players_query]
    players = json.dumps(players_list)

    return render_template('api/player_stats_usage.html',
                            title="NBA Player Stats API Usage",
                            players=players)



@api.route("/nba_stats", methods=['GET'])
def nba_stats_api():

    try:
        player_name = request.args['player']
    except:
        return "Add a query parameter for player: '?player=LeBron James (F)'"

    player_stats = NBA_Player_Stats.query.filter_by(name=player_name).all()

    player_object = {
        player_name: []
    }

    if len(player_stats) == 0:
        player_names_url = url_for('api.nba_players')
        line1 = "<p>You spelled the name wrong or that player doesn't exist<p>"
        line2 = "<p>Check here for the player spelling: <p>"
        line3 = f'<a href="{player_names_url}">players</a>'
        return line1 + line2 + line3

    else:
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


@api.route("/nba_player_info/usage", methods=['GET'])
def nba_player_info_api_usage():
    return render_template('api/player_info_usage.html',
                            title="NBA Player Info API Usage")


@api.route("/nba_player_info", methods=['GET'])
def nba_player_info_api():

    try:
        player_name = request.args['player']
    except:
        return "Add a query parameter for player: '?player=LeBron James'"


    player_info = NBA_Player_Info.query.filter_by(name=player_name).first()

    if player_info:
        player_object = {
            player_name: {
                'position': player_info.position,
                'age': player_info.age,
                'height': player_info.height,
                'weight': player_info.weight,
                'college': player_info.college,
                'salary': player_info.salary
            }
        }
    else:
        return "You spelled the name wrong or that player doesn't exist"

    return jsonify(player_object)
