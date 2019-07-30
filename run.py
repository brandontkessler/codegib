import os
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, NBA_Player_Stats, NBA_Player_Info, Blog

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db,
                User=User,
                Blog=Blog,
                NBA_Player_Stats=NBA_Player_Stats,
                NBA_Player_Info=NBA_Player_Info)
