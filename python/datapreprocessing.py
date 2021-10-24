#import requests
import pandas as pd
import data
from data import refreshData
from manipulation import *

pd.options.mode.chained_assignment = None  # default='warn'

# resolves all missing data in the dataframes
def fixMissingValues():
    fixGeneralInfoMissingValues()
    fixFixturesMissingValues()

def fixGeneralInfoMissingValues():
    dropEmptyValueRow(data.events_user_scored_df)
    dropEmptyValueRow(data.events_user_management_df)
    dropColumnByName(data.teams_df, 'team_division')
    fillEmptyValueColumn(data.player_set_piece_df, 0)
    dropEmptyValueRow(data.player_news_df)
    data.player_chance_of_playing_df = data.player_chance_of_playing_df[data.player_chance_of_playing_df.status != 'a'] # removes all 100% available players from the data frame
    fillEmptyValueColumn(data.player_chance_of_playing_df, 0)

def fixFixturesMissingValues():
    dropEmptyValueRow(data.fixtures_scores_df)

def addNewData():
    calculateTeamFdr()

def calculateTeamFdr():
    fdr_dict_temp = {'event': [], 'team_id': [], 'fdr': []}
    for team in data.teams_df['id']:
        for event in data.events_df['id']:
            fdr_temp = data.fixtures_df[['event', 'team_h', 'team_h_difficulty', 'team_a', 'team_a_difficulty']]
            fdr_temp = fdr_temp[(fdr_temp["event"].isin([event, event + 1, event + 2])) & ((fdr_temp["team_h"] == team) | (fdr_temp["team_a"] == team))]
            fdr_count_temp = 0
            fixture_count_temp = 0
            for fixture in fdr_temp.values:
                fixture_count_temp += 1
                if fixture[1] == team:
                    fdr_count_temp += fixture[2]
                else:
                    fdr_count_temp += fixture[4]
            fdr_dict_temp.get('event').append(event)
            fdr_dict_temp.get('team_id').append(team)
            fdr_dict_temp.get('fdr').append(round(fdr_count_temp/fixture_count_temp, 1))

    data.team_fdr = pd.DataFrame(fdr_dict_temp).sort_values(by=['event', 'team_id'], ignore_index=True)

def calculateForm():
    return

def preprocess():
    refreshData()
    fixMissingValues()
    addNewData()