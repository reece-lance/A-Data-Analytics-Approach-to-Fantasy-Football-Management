import requests
import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None  # default='warn'

# JSON variables
general_info_json = None
fixtures_json = None

# data frames and variables from general_info_json
events_df = None
data_not_checked_df = None
general_events_info_df = None
general_events_stats_df = None
game_settings_dict = {}
phases_df = None
teams_df = None
total_players = 0
elements_df = None
chance_of_playing_df = None
element_stats_df = None
element_types_df = None

# data frames and variables from fixtures_json

# fetches data stored at a URL
def fetchData(url):
    try:
        r = requests.get(url)
        return r.json()
    except:
        return None

# creates all data frames
def createDataFrames():
    createGeneralInfoDataFrames()

# creates all data frames from the general_info_json
def createGeneralInfoDataFrames():
    global events_df, data_not_checked_df, general_events_info_df, general_events_stats_df, game_settings_dict, hases_df, teams_df, total_players, elements_df, chance_of_playing_df, element_stats_df, element_types_df

    events_df = pd.DataFrame(general_info_json['events'])

    data_checked = events_df.groupby(events_df.finished)
    data_not_checked_df = data_checked.get_group(False)

    general_events_info_df = events_df[['id', 'name', 'deadline_time', 'is_previous', 'is_current', 'is_next', 'finished', 'data_checked']]

    game_settings_dict = general_info_json.get('game_settings')

    phases_df = pd.DataFrame(general_info_json['phases'])

    teams_df = pd.DataFrame(general_info_json['teams'])

    total_players = general_info_json.get('total_players')

    elements_df = pd.DataFrame(general_info_json['elements'])

    chance_of_playing_df = elements_df[['id', 'status', 'chance_of_playing_this_round', 'chance_of_playing_next_round']]
    chance_of_playing_df = chance_of_playing_df[chance_of_playing_df.status != 'a'] # removes all 100% available players from the data frame

    element_stats_df = pd.DataFrame(general_info_json['element_stats'])

    element_types_df = pd.DataFrame(general_info_json['element_types'])

# removes whole column from data frame if column has any missing values
def dropEmptyValueColumn(dataFrame):
    try:
        dataFrame.dropna(inplace=True, axis=1)
    except:
        pass

# replaces empty values in columns from the data frame with new value
def fillEmptyValueColumn(dataFrame, newValue):
    try:
        dataFrame.fillna(newValue, inplace=True)
    except:
        pass

# removes whole column from data frame by name
def dropColumnByName(dataFrame, columnName):
    try:
        dataFrame.drop(columnName, inplace=True, axis=1)
    except:
        pass

# 
def fixMissingValues():
    global data_not_checked_df, teams_df, chance_of_playing_df

    dropEmptyValueColumn(data_not_checked_df)

    dropColumnByName(teams_df, 'team_division')

    fillEmptyValueColumn(chance_of_playing_df, 0)

if __name__ == "__main__":
    general_info_json = fetchData('https://fantasy.premierleague.com/api/bootstrap-static/')
    fixtures_json = fetchData('https://fantasy.premierleague.com/api/fixtures/')
    createDataFrames()
    fixMissingValues()