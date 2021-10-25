#import requests
import pandas as pd
import data
from data import refreshData
from manipulation import *

pd.options.mode.chained_assignment = None  # default='warn'

def preprocess():
    refreshData()
    fixMissingValues()
    addNewData()

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
    calculateTeamForm()

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

    data.team_fdr_df = pd.DataFrame(fdr_dict_temp).sort_values(by=['event', 'team_id'], ignore_index=True)

def calculateTeamForm():
    team_form_dict_temp = {'event': [], 'team': [], 'form': []}
    data_checked_events_temp = data.events_df['id']
    data_checked_events_temp = data_checked_events_temp[data.events_df['data_checked'] == True]
    for team in data.teams_df['id']:
        for event in data_checked_events_temp:
            form_temp = data.fixtures_df[['event', 'team_h', 'team_h_score', 'team_h_difficulty', 'team_a', 'team_a_score', 'team_a_difficulty']]
            form_temp = form_temp[(form_temp['event'].isin([event, event - 1, event - 2, event - 3, event - 4])) & ((form_temp['team_h'] == team) | (form_temp['team_a'] == team))]
            form_count_temp = 0
            for fixture in form_temp.values:
                if fixture[1] == team:
                    if fixture[2] > fixture[5]:
                        form_count_temp += fixture[3]
                    elif fixture[2] < fixture[5]:
                        form_count_temp -= fixture[6]
                    else:
                        form_count_temp += (fixture[3] - 3)
                elif fixture[4] == team:
                    if fixture[2] < fixture[5]:
                        form_count_temp += fixture[6]
                    elif fixture[2] > fixture[5]:
                        form_count_temp -= fixture[3]
                    else:
                        form_count_temp += (fixture[6] - 3)
        team_form_dict_temp.get('event').append(event)
        team_form_dict_temp.get('team').append(team)
        team_form_dict_temp.get('form').append(form_count_temp)

        data.team_form_df = pd.DataFrame(team_form_dict_temp).sort_values(by=['event', 'team'], ignore_index=True)

def calculatePlayerForm():
    return