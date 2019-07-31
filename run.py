import os
from app import create_app, db
from app.models import User, NBA_Player_Stats, NBA_Player_Info, Blog

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.shell_context_processor
def make_shell_context():
    return dict(db=db,
                User=User,
                Blog=Blog,
                NBA_Player_Stats=NBA_Player_Stats,
                NBA_Player_Info=NBA_Player_Info)


@app.cli.command('add_api_data')
def add_api_data_command():
    """Adds standalone api data to database."""

    # Imports
    from api_data.api_data import (create_nba_stats_to_inject,
        create_nba_player_info_to_inject)

    # Create objects to import
    stats_objects = create_nba_stats_to_inject('api_data/nba/player_stats_2019', NBA_Player_Stats)
    info_objects = create_nba_player_info_to_inject('api_data/nba/player_info', NBA_Player_Info)

    # Add to db session
    db.session.add_all(stats_objects)
    db.session.add_all(info_objects)

    # Commit session
    db.session.commit()
    print("Added all API data")


@app.cli.command('add_seed')
def add_seed_command():
    """Adds seed data to database."""

    from seed import create_seed_users, create_seed_blogs

    create_seed_users(db, User)
    create_seed_blogs(db, Blog)

    db.session.commit()
    print("Added seed data")
