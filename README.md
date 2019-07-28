# Setting up the database


### NBA API SETUP

Make sure the csv files are located in the api_data/nba directory.

```
$ flask shell

>>> from api_data.api_data import create_nba_stats_to_inject
>>> objects = create_nba_stats_to_inject('api_data/nba', NBA_Player_Stats)
>>> db.session.add_all(objects)
>>> db.session.commit()
>>> exit()
```
