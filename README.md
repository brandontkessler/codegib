# INITIALIZING THE APP

```
$ export FLASK_APP=run.py
$ export FLASK_DEBUG=True
```

# SETTING UP THE DATABASE

## Create the database:

Using postgres:

```
$ psql postgres -U <username>

=> CREATE DATABASE <db name>;
=> \q
```

Note that you should create a test database as well...

## Create Tables

```
$ flask shell

>>> db.create_all()
>>> exit()
```

### ADD STANDALONE API DATA AND/OR SEED DATA TO DB

To do this, we can use two options. The preferred option is using the provided CLI commands directly in the terminal. Otherwise we can manually load the data through flask shell.

#### Option 1: Use provided cli commands

```
$ flask add_nba_stats
$ flask add_nba_info
$ flask add_seed_users
$ flask add_seed_blogs
```


#### Option 2: Setup manually from flask shell

**NBA PLAYER STATS API SETUP:**

Make sure the csv files are located in the "api_data/nba/player_stats_2019" directory.

```
$ flask shell

>>> from api_data.api_data import create_nba_stats_to_inject as p_stats
>>> objects = p_stats('api_data/nba/player_stats_2019', NBA_Player_Stats)
>>> db.session.add_all(objects)
>>> db.session.commit()
>>> exit()
```


**NBA PLAYER INFO API SETUP:**

Make sure the csv files are located in the "api_data/nba/player_info" directory.

```
$ flask shell

>>> from api_data.api_data import create_nba_player_info_to_inject as p_info
>>> objects = p_info('api_data/nba/player_info', NBA_Player_Info)
>>> db.session.add_all(objects)
>>> db.session.commit()
>>> exit()
```


**USING AVAILABLE SEED DATA:**

```
$ flask shell

>>> from seed import create_seed_users, create_seed_blogs
>>> create_seed_users(db, User)
>>> create_seed_blogs(db, Blog)
>>> db.session.commit()
>>> exit()
```


---

# UPDATING SCHEMAS/DATABASE

This does not use Alembic for migrations so changes must be updated manually. Using a postgresql database, we can make changes to our models and update directly against the database:

**Example using PostgresQL as database management:**

Start by adding the column to the table in the database directly through psql:

```
$ psql postgres -U <username>

=> ALTER TABLE <table name>
-> ADD COLUMN <column name>
-> <type (VARCHAR, INTEGER, etc.)> <(optional) NOT NULL>
-> DEFAULT <default value>;
```

*Note:* A default value must be included if using 'NOT NULL', otherwise a column that requires a value will try to be created without one.


Next, we can update the Flask model to include the changes:

```
class Model_to_Update(db.Model):

    ...

    <column name> = db.Column(db.<Integer>, nullable=<False>, <default=0>)

    ...
```

Now in the terminal we can restart the app with `$ flask run` and the database will be working correctly.



# FEATURED ARTICLES

## The carousel

The carousel content is managed through a table called carousel. It does not only include CodeGib content, but also includes external. Therefore, the table does not contain a foreign key and is not linked to other tables.

Images for these articles are stored under 'static/img/carousel'.

These must be updated manually. After the database is created, these can be added through the shell command (similar to the seed/api data) with below:


**LOADING INITIAL CAROUSEL ARTICLES:**

```
$ flask add_initial_carousel_items
```

When adding carousel articles, if using articles from CodeGib, the url should only include the name of the article itself and the source must be 'CodeGib'.



## Top 3 on Homepage

The top 3 articles that are featured on the homepage are chosen manually. This can be changed by altering the index route and selecting a new blog to replace the ones currently selected.
