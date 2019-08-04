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


@app.cli.command('add_nba_stats')
def add_nba_stats_command():
    from api_data.api_data import (create_nba_stats_to_inject)

    stats_objects = create_nba_stats_to_inject('api_data/nba/player_stats_2019', NBA_Player_Stats)

    db.session.add_all(stats_objects)
    db.session.commit()
    print("Added NBA Stats API data")


@app.cli.command('add_nba_info')
def add_nba_stats_command():
    from api_data.api_data import (create_nba_player_info_to_inject)

    info_objects = create_nba_player_info_to_inject('api_data/nba/player_info', NBA_Player_Info)

    db.session.add_all(info_objects)
    db.session.commit()
    print("Added NBA Info API data")


@app.cli.command('add_seed_users')
def add_seed_users_command():
    from seed import create_seed_users

    create_seed_users(db, User)

    db.session.commit()
    print("Added seed user data")


@app.cli.command('add_seed_blogs')
def add_seed_command():
    from seed import create_seed_blogs

    create_seed_blogs(db, Blog)

    db.session.commit()
    print("Added seed blog data")


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
