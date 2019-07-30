# Setting up the database

### CREATE TABLES

```
$ flask shell

>>> db.create_all()
>>> exit()
```

### INITIALIZE MIGRATIONS

```
$ flask db init
```


### NBA PLAYER STATS API SETUP

Make sure the csv files are located in the "api_data/nba/player_stats_2019" directory.

```
$ flask shell

>>> from api_data.api_data import create_nba_stats_to_inject as p_stats
>>> objects = p_stats('api_data/nba/player_stats_2019', NBA_Player_Stats)
>>> db.session.add_all(objects)
>>> db.session.commit()
>>> exit()
```


### NBA PLAYER INFO API SETUP

Make sure the csv files are located in the "api_data/nba/player_info" directory.

```
$ flask shell

>>> from api_data.api_data import create_nba_player_info_to_inject as p_info
>>> objects = p_info('api_data/nba/player_info', NBA_Player_Info)
>>> db.session.add_all(objects)
>>> db.session.commit()
>>> exit()
```
