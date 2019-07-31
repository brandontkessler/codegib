# SETTING UP THE DATABASE

## CREATE TABLES

```
$ flask shell

>>> db.create_all()
>>> exit()
```

## ADD STANDALONE API DATA TO DB

### Option 1: Use provided cli commands

```
$ flask add_api_data
$ flask add_seed
```


### Option 2: Setup manually from flask shell

##### NBA PLAYER STATS API SETUP

Make sure the csv files are located in the "api_data/nba/player_stats_2019" directory.

```
$ flask shell

>>> from api_data.api_data import create_nba_stats_to_inject as p_stats
>>> objects = p_stats('api_data/nba/player_stats_2019', NBA_Player_Stats)
>>> db.session.add_all(objects)
>>> db.session.commit()
>>> exit()
```


##### NBA PLAYER INFO API SETUP

Make sure the csv files are located in the "api_data/nba/player_info" directory.

```
$ flask shell

>>> from api_data.api_data import create_nba_player_info_to_inject as p_info
>>> objects = p_info('api_data/nba/player_info', NBA_Player_Info)
>>> db.session.add_all(objects)
>>> db.session.commit()
>>> exit()
```


##### USING AVAILABLE SEED DATA

```
$ flask shell

>>> from seed import create_seed_users, create_seed_blogs
>>> create_seed_users(db, User)
>>> create_seed_blogs(db, Blog)
>>> db.session.commit()
>>> exit()
```
