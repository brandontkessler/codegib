import os
import pandas as pd


# CSV File Generator
def csv_generator(path):
    for root, dirnames, filenames in os.walk(path):
        for file_name in filenames:
            filepath = os.path.join(root, file_name)
            file = pd.read_csv(filepath)

            yield file


# Append dataframes
def df_from_directory(path):
    df = pd.DataFrame()

    for file in csv_generator(path):
        df = df.append(file)
    return df


def date_converter(pd_series):
    dates = {date:pd.to_datetime(date) for date in pd_series}
    return pd_series.map(dates)


###########################################
# NBA DATA
def create_nba_stats_to_inject(path, db_schema):
    nba_df = df_from_directory(path)
    nba_df['date'] = date_converter(nba_df['date'])

    objects = []

    for index, row in nba_df.iterrows():
        item = db_schema(
            date = row['date'],
            game_type = row['game_type'],
            team = row['team'],
            opponent = row['opponent'],
            home = row['home'],
            name = row['name'],
            minutes = row['minutes'],
            points = row['points'],
            rebounds = row['rebounds'],
            assists = row['assists'],
            steals = row['steals'],
            blocks = row['blocks'],
            fouls = row['fouls'],
            turnovers = row['turnovers'],
            o_rebounds = row['o_rebounds'],
            d_rebounds = row['d_rebounds'],
            fg_made = row['fg_made'],
            fg_att = row['fg_att'],
            ft_made = row['ft_made'],
            ft_att = row['ft_att'],
            three_pts_made = row['three_pts_made'],
            three_pts_att = row['three_pts_att'],
            plus_minus = row['plus_minus']
        )
        objects.append(item)

    return objects
