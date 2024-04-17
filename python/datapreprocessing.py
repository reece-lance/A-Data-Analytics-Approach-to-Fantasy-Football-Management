import pandas as pd
import data
from data import refreshData
from data import getPlayerGameweekData
from manipulation import *
import appconstants
import os
import unidecode
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'

def preprocess():
    refreshData()
    fixMissingValues()
    addNewData()
    predictPreprocess()

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
    calculateTeamsMissingValues()
    calculateTeamFdr()
    calculateTeamForm()

def calculateTeamsMissingValues():
    data.teams_df["goals_for"] = 0
    data.teams_df["goals_against"] = 0
    data.teams_df["goal_difference"] = 0

    started_fixtures = data.fixtures_df[['team_h', 'team_h_score', 'team_a', 'team_a_score']]
    started_fixtures = started_fixtures[data.fixtures_df['minutes'] != 0]

    for index, row in started_fixtures.iterrows():
        data.teams_df.at[row['team_h']-1, 'played'] += 1
        data.teams_df.at[row['team_a']-1, 'played'] += 1
        if row['team_h_score'] > row['team_a_score']:
            data.teams_df.at[row['team_h']-1, 'win'] += 1
            data.teams_df.at[row['team_a']-1, 'loss'] += 1
            data.teams_df.at[row['team_h']-1, 'points'] += 3

        elif row['team_h_score'] == row['team_a_score']:
            data.teams_df.at[row['team_h']-1, 'draw'] += 1
            data.teams_df.at[row['team_a']-1, 'draw'] += 1
            data.teams_df.at[row['team_h']-1, 'points'] += 1
            data.teams_df.at[row['team_a']-1, 'points'] += 1

        else:
            data.teams_df.at[row['team_a']-1, 'win'] += 1
            data.teams_df.at[row['team_h']-1, 'loss'] += 1
            data.teams_df.at[row['team_a']-1, 'points'] += 3
    
        data.teams_df.at[row['team_h']-1, 'goals_for'] += int(row['team_h_score'])
        data.teams_df.at[row['team_a']-1, 'goals_for'] += int(row['team_a_score'])

        data.teams_df.at[row['team_h']-1, 'goals_against'] += int(row['team_a_score'])
        data.teams_df.at[row['team_a']-1, 'goals_against'] += int(row['team_h_score'])

    for index, row in data.teams_df.iterrows():
        data.teams_df.at[index, 'goal_difference'] = int(row['goals_for'] - row['goals_against'])

    for index, row in data.teams_df.sort_values(by=['points', 'goal_difference', 'goals_for'], ascending=False, ignore_index=True).iterrows():
        data.teams_df.at[row['id']-1, 'position'] = index + 1

    data.teams_results_df = data.teams_df[['code', 'position', 'played', 'win', 'draw', 'loss', 'points']]

    addTeamBadge()

def addTeamBadge():
    badge_dict = {}
    for team in data.teams_df['id']:
        badge_dict[team] = os.path.join(appconstants.badgesPath, str(team) + ".png")

    data.teams_df['badge'] = data.teams_df['id'].map(badge_dict)

def calculateTeamFdr():
    fdr_dict_temp = {'event': [], 'team': [], 'fdr': []}
    for team in data.teams_df['id']:
        for event in data.events_df['id']:
            fdr_temp = data.fixtures_df[['event', 'team_h', 'team_h_difficulty', 'team_a', 'team_a_difficulty']]
            fdr_temp = fdr_temp[(fdr_temp["event"].isin([event, event + 1, event + 2])) & ((fdr_temp["team_h"] == team) | (fdr_temp["team_a"] == team))] # next 3 events, if team play
            fdr_count_temp = 0
            fixture_count_temp = 0
            for fixture in fdr_temp.values:
                fixture_count_temp += 1
                if fixture[1] == team: # if home team
                    fdr_count_temp += fixture[2]
                else: # if away team
                    fdr_count_temp += fixture[4]
            fdr_dict_temp.get('event').append(event)
            fdr_dict_temp.get('team').append(team)
            try:
                fdr_dict_temp.get('fdr').append(round(fdr_count_temp/fixture_count_temp, 1))
            except:
                fdr_dict_temp.get('fdr').append(0)

    data.team_fdr_df = pd.DataFrame(fdr_dict_temp).sort_values(by=['event', 'team'], ignore_index=True)

def calculateTeamForm():
    team_form_dict_temp = {'event': [], 'team': [], 'form': []}
    data_checked_events_temp = data.events_df['id']
    data_checked_events_temp = data_checked_events_temp[data.events_df['data_checked'] == True]
    for team in data.teams_df['id']:
        for event in data_checked_events_temp:
            form_temp = data.fixtures_df[['event', 'team_h', 'team_h_score', 'team_h_difficulty', 'team_a', 'team_a_score', 'team_a_difficulty']]
            form_temp = form_temp[(form_temp['event'].isin([event, event - 1, event - 2, event - 3, event - 4])) & ((form_temp['team_h'] == team) | (form_temp['team_a'] == team))] # last 5 events, if team played
            form_count_temp = 0
            for fixture in form_temp.values:
                if fixture[1] == team: # if home team
                    if fixture[2] > fixture[5]: # home team win
                        form_count_temp += fixture[3]
                    elif fixture[2] < fixture[5]: # home team lose
                        form_count_temp -= fixture[6]
                    else: # draw
                        form_count_temp += (fixture[3] - 3)
                elif fixture[4] == team: # if away team
                    if fixture[2] < fixture[5]: # away team win
                        form_count_temp += fixture[6]
                    elif fixture[2] > fixture[5]: # away team lose
                        form_count_temp -= fixture[3]
                    else: # draw
                        form_count_temp += (fixture[6] - 3)
        team_form_dict_temp.get('event').append(event)
        team_form_dict_temp.get('team').append(team)
        team_form_dict_temp.get('form').append(form_count_temp)

        data.team_form_df = pd.DataFrame(team_form_dict_temp).sort_values(by=['event', 'team'], ignore_index=True)

def getInitialTeamFromDf(df, sort, teamDf, budget):
    if sort != None:
        df = df.sort_values(by=[sort], ascending=False)
        df = df.reset_index(drop=True)
    df = df[['id']]
    df['rank'] = df.index
    noPerPos = {1 : 2, 2 : 5, 3 : 5, 4 : 3}
    df['element_type'] = df.id.map(data.elements_df.set_index('id').element_type) # maps the players' positions from elements_df
    posDict = {1 : 0, 2 : 0, 3 : 0, 4 : 0}
    df['team'] = df.id.map(data.elements_df.set_index('id').team) # maps the players' team from elements_df
    teamDict = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0, 15 : 0, 16 : 0, 17 : 0, 18 : 0, 19 : 0, 20 : 0}
    newlyAdded = []

    if len(teamDf.index) > 0:
        teamDf['element_type'] = teamDf.id.map(data.elements_df.set_index('id').element_type)
        teamDf['team'] = teamDf.id.map(data.elements_df.set_index('id').team)
        for c in teamDf.index:
            posDict[teamDf['element_type'][c]] += 1
            teamDict[teamDf['team'][c]] += 1

        teamCost = sum(teamDf.id.map(data.elements_df.set_index('id').start_cost))
    else:
        teamCost = 0

    for n in df.index:
        newPlayer = df.iloc[[n]]
        newPlayerPos = df['element_type'][n]
        newPlayerTeam = df['team'][n]
        newPlayerCost = newPlayer.id.map(data.elements_df.set_index('id').start_cost).get(n)
        if len(teamDf.index) < 15:
            if posDict.get(int(newPlayerPos)) < noPerPos.get(int(newPlayerPos)) and teamDict.get(int(newPlayerTeam)) < 3 and (teamCost + newPlayerCost) <= budget:
                posDict[newPlayerPos] += 1
                teamDict[newPlayerTeam] += 1
                teamCost += newPlayerCost
                teamDf = teamDf.append(df.iloc[n])
                teamDf = teamDf.reset_index(drop=True)
        else:
            for c in reversed(teamDf.index):
                if c not in newlyAdded:
                    currentPlayer = teamDf.iloc[[c]]
                    currentPlayerCost = currentPlayer.id.map(data.elements_df.set_index('id').start_cost).get(c)
                    if n < teamDf['rank'][c] or (n == teamDf['rank'][c] and newPlayerCost < currentPlayerCost):
                        currentPlayerPos = teamDf['element_type'][c]
                        currentPlayerTeam = teamDf['team'][c]
                        if newPlayerPos == currentPlayerPos and (newPlayerTeam == currentPlayerTeam or teamDict.get(int(newPlayerTeam)) < 3) and df['id'][n] not in teamDf['id'].tolist() and (teamCost + newPlayerCost - currentPlayerCost) <= budget:
                            teamDict[currentPlayerTeam] -= 1
                            teamDict[newPlayerTeam] += 1
                            teamCost += (newPlayerCost - currentPlayerCost)
                            newlyAdded.append(c)
                            teamDf.iloc[c] = df.iloc[n]
                            break
            

    teamDf = teamDf[['id', 'rank']]
    teamDf['id'] = teamDf['id'].astype(int)
    teamDf['rank'] = teamDf['rank'].astype(int)
    return teamDf

# TABLES

def createFixturesDf():
    df = data.fixtures_df[['kickoff_time', 'team_h', 'team_a']]
    df = df[data.fixtures_df['minutes'] == 0]
    df['vs'] = 'vs'
    df['badge_h'] = df.team_h.map(data.teams_df.set_index('id').badge)
    df['badge_a'] = df.team_a.map(data.teams_df.set_index('id').badge)
    df['team_h'] = df.team_h.map(data.teams_df.set_index('id').name)
    df['team_a'] = df.team_a.map(data.teams_df.set_index('id').name)
    df[['date','time']] = df['kickoff_time'].str.split('T',expand=True)
    df['time'] = df['time'].str[:-4]
    df['date'] = df['date'].fillna('TBC')
    df['time'] = df['time'].fillna('TBC')
    return df[['date', 'time', 'team_h', 'badge_h', 'vs', 'badge_a', 'team_a']]

# SIGN IN METHODS

def createTeam(df, event):
    df['name'] = df.element.map(data.elements_df.set_index('id').web_name)
    df['photo'] = df.element.map(data.elements_df.set_index('id').photo)
    df['team_name'] = df.element.map(data.elements_df.set_index('id').team)
    df['team_name'] = df.team_name.map(data.teams_df.set_index('id').short_name)
    df['position_name'] = df.element.map(data.elements_df.set_index('id').element_type)
    df['position_name'] = df.position_name.map(data.element_types_df.set_index('id').singular_name_short)
    player_data_list = getPlayerGameweekData(event)

    teams_points = []
    for element in df['element']:
        player_multiplier = int(df.loc[df['element'] == element, 'multiplier'])
        if player_multiplier == 0:
            player_multiplier = 1
        try:
            teams_points.append(player_data_list[element-1].get('stats').get('total_points') * player_multiplier)
        except:
            teams_points.append(0)
    
    df['points'] = teams_points
    df['is_captain'] = df['is_captain'].replace([True, False], ['C', None])
    df['is_vice_captain'] = df['is_vice_captain'].replace([True, False], ['VC', ''])
    df['special'] = df['is_captain'].fillna(df['is_vice_captain'])

    return df[['position', 'photo', 'name', 'team_name', 'position_name', 'points', 'special']]

def createMyManagerData():
    data.manager_basic_info_list = createManagerBasicInfoList(data.manager_basic_info_json)
    createManagerHistoryDict(data.manager_history_dict, data.manager_history_json)

def createManagerBasicInfoList(jsonData):
    return createManagerList(
            jsonData,
            ['player_first_name', 'started_event', 'summary_overall_points', 'summary_overall_rank', 'last_deadline_value', 'last_deadline_bank'],
            ['Name', 'First Event', 'Overall Points', 'Overall Rank', 'Team Value', 'Balance'])

def createManagerHistoryDict(dict, jsonData):
    for event in range(len(data.manager_gameweeks)):
        dict[jsonData['current'][event].get('event')] = createManagerList(
            jsonData['current'][event],
            ['points', 'total_points', 'rank', 'bank', 'value', 'event_transfers', 'event_transfers_cost', 'points_on_bench'],
            ['Points', 'Total Points', 'Rank', 'Balance', 'Team Value', 'Transfers', 'Transfers Cost', 'Points On Bench'])

    return dict

def createManagerList(data, keys, newKeys):
    dict_list = []

    values = []
    for key in keys:
        value = getValue(data, key)
        if key in ['bank', 'value', 'event_transfers_cost', 'last_deadline_value', 'last_deadline_bank']:
            value = getHistoryMoneyValue(value)
        elif key in ['summary_overall_rank', 'rank']:
            value = getRank(str(value))
        values.append(value)

    for i in range(len(keys)):
        row = {}
        row['keys'] = newKeys[i]
        row['values'] = values[i]
        dict_list.append(row)

    return dict_list

def getValue(data, key):
    return data.get(key)

def getHistoryMoneyValue(value):
    return '£' + str(value/10) + 'M'

def getRank(value):
    if value[-1] == '1':
        return value + 'st'
    elif value[-1] == '2':
        return value + 'nd'
    elif value[-1] == '3':
        return value + 'rd'
    else:
        return value + 'th'

def predictPreprocess():
    for col in data.players_df.keys():
        if data.players_df[col].isnull().values.any():
            dropColumnByName(data.players_df, col)

    data.players_df['position'] = data.players_df.element_type.map({1 : 'Keeper', 2 : 'Defender', 3 : 'Midfielder', 4 : 'Forward'})
    data.players_df['starting_cost'] = data.players_df.now_cost - data.players_df.cost_change_start_fall
    data.players_df['cost_bin'] = data.players_df.now_cost.apply(lambda x: np.floor(x/10))
    data.players_df['full_name'] = data.players_df.apply(lambda x: get_full_name_playerdf(x.first_name, x.second_name), axis=1).str.lower()


    data.gameweek_fixture_df['full_name'] = data.gameweek_fixture_df.name.str.replace('_\d+','')
    data.gameweek_fixture_df['full_name'] = data.gameweek_fixture_df['full_name'].str.replace(" ", "_").str.replace("-", "_").str.replace('_\d+','')
    data.gameweek_fixture_df['full_name'] = data.gameweek_fixture_df['full_name'].apply(lambda x: unidecode.unidecode(x))
    data.gameweek_fixture_df['full_name'] = data.gameweek_fixture_df['full_name'].str.lower()

    data.player_positions = data.players_df[['full_name', 'position']].drop_duplicates(subset = ['full_name'], keep = 'last').reset_index(drop = True)

    unique_players=[]
    dup_players=[]
    for player in data.players_df[['code', 'full_name']].drop_duplicates(subset='code')['full_name']:
        if player not in unique_players:
            unique_players.append(player)
        else:
            dup_players.append(player)

    data.players_df = data.players_df[~data.players_df['full_name'].isin(dup_players)]
    data.gameweek_fixture_df = data.gameweek_fixture_df[~data.gameweek_fixture_df['full_name'].isin(dup_players)]

    data.players_df['player_team_name'] = data.players_df['team_code'].replace(data.team_codes_df.team_code.unique(), data.team_codes_df.name.unique())
    data.gameweek_fixture_df = clean_gw_df(data.players_df, data.gameweek_fixture_df, data.team_codes_df)

    data.current_season_player_df = data.players_df[data.players_df.season == appconstants.CURRENT_SEASON] 
    data.previous_season_player_df = data.players_df[data.players_df.season == appconstants.LAST_SEASON]

    data.available_players_df = getCurrentSeasonsDf(data.current_season_player_df, data.previous_season_player_df)

    for col in data.available_players_df.keys():
        if data.available_players_df[col].isnull().values.any():
            dropColumnByName(data.available_players_df, col)

    data.gameweek_fixture_df['team_points']= data.gameweek_fixture_df.apply(lambda x: get_team_points(x.was_home, x.team_h_score, x.team_a_score), axis=1)
    data.gameweek_fixture_df['opponent_points'] = data.gameweek_fixture_df.team_points.apply(lambda x: get_opponent_points(x))

def get_full_name_playerdf(first_name, second_name):
    full_name = first_name +'_' + second_name
    full_name = full_name.replace(" ", "_")
    full_name = full_name.replace("-", "_")
    full_name = unidecode.unidecode(full_name)
    
    return full_name

# Returns a df with player position, player's team name, and opponent's team name
def clean_gw_df(player_df, gw_df, team_codes_df):
    pdf = player_df.copy()[['full_name', 'season', 'position', 'player_team_name']]
    gdf = gw_df.copy()
    
    gdf = gdf.merge(pdf, on=['full_name', 'season', 'position'], how='left')
    dfs = []
    for season, group in gdf.groupby('season'):
        group['opponent_team_name'] = group['opponent_team'].replace(team_codes_df[team_codes_df['season'] == season].team.unique(), team_codes_df[team_codes_df['season'] == season].name.unique())
        dfs.append(group[['opponent_team_name']])
        
    out_df = pd.concat(dfs, axis=0)
    out_df = pd.concat([gdf, out_df], axis=1)

    return out_df

def getCurrentSeasonsDf(this_season_player_df, last_season_player_df):
    last_season_player_df = last_season_player_df[last_season_player_df.minutes > 0][['full_name', "total_points"]]
    last_season_player_df.rename(columns={'total_points': "prev_total_points"}, inplace=True)
    
    available_players_df = pd.merge(this_season_player_df, last_season_player_df, on='full_name', how='left')
    
    available_players_df.prev_total_points = available_players_df.groupby(['position', 'cost_bin']).prev_total_points.transform(lambda x: x.fillna(x.mean()))

    dropEmptyValueRow(available_players_df)
    
    return available_players_df.reset_index(drop=True)

def get_team_points(home, home_score, away_score):
    try:
        if home_score > away_score:
            if home:
                return 3
            else: 
                return 0
        if home_score < away_score:
            if home:
                return 0
            else: 
                return 3
        else:
            return 1
    except:
        return -1

def get_opponent_points(team_points):
    if team_points == 3:
        return 0
    elif team_points == 1:
        return 1
    elif team_points == 0:
        return 3
    else:
        return -1