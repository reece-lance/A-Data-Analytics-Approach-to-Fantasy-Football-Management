import pandas as pd
import appconstants
from api import fetchData
from managejson import fetchStoredData
from managejson import storeJson
import manipulation

live = False

# JSON data
general_info_json = fixtures_json = None

# GENERAL INFO
# Events
events_df = events_general_info_df = events_deadline_df = events_user_scored_df = events_user_management_df = None
previous_event_int = current_event_int = next_event_int = 0
# Game Settings
game_settings_full_dict = None
# Phases
phases_df = None
# Teams
teams_df = teams_results_df = teams_name_df = teams_short_name_df = teams_rating_df = teams_unavailable_df = teams_pulse_id_df = None
# Total Players
total_players_int = 0
# Elements
elements_df = player_id_df = player_team_position_df = player_cost_df = player_status_df = player_points_df = player_user_transfers_df = player_stats_df = player_value_df = player_ep_ict_df = player_set_piece_df = player_news_df = player_dreamteam_df = player_chance_of_playing_df = player_status_df = None
not_unavailable_elements_df = available_elements_df = None
# Element Stats
element_stats_df = None
# Element Types
element_types_df = None

# FIXTURES
fixtures_df = fixtures_event_code_df = fixtures_timings_df = fixtures_teams_df = fixtures_scores_df = fixtures_difficulty_df = None

upcoming_fixtures = None

# USEFUL
upcoming_event_int = 0

# CUSTOM
team_fdr_df = team_form_df = None

# Manager Data (only available if signed in)

manager_team_dict = {}
pred_team_dict = {}

manager_gameweeks = []
prediction_gameweeks = []

manager_security_json = None

manager_basic_info_json = None
manager_history_json = None

manager_basic_info_list = []
manager_history_dict = {}

manager_current_team_json = None

players_df = None
gameweek_fixture_df = None
team_codes_df = None

player_positions = None
available_players_df = None
current_season_player_df = None
previous_season_player_df = None

bench_players = []
initial_team_df = None
bench_cost = 0

lagged_gw_df = None
relevant_features = []
numerical_features = []
categorical_features = None

test_df = None
X_train = None
y_train = None
X_test = None
y_test = None

predicted_df_lin_reg = None

def refreshData():
    global general_info_json, fixtures_json
    general_info_json = fetchData(appconstants.generalInfoUrl, appconstants.generalInfoJsonDir)
    fixtures_json = fetchData(appconstants.fixturesUrl, appconstants.fixturesJsonDir)
    if general_info_json != None and fixtures_json != None:
        createDataFrames()
    else:
        print('Error: Cannot refresh data')

# creates all data frames
def createDataFrames():
    createGeneralInfoDataFrames()
    createEventsDataFrames()
    createTeamsDataFrames()
    createElementsDataFrames()
    createFixturesDataFrame()
    predictData()

# creates all data frames from the general_info_json
def createGeneralInfoDataFrames():
    global game_settings_full_dict, phases_df, total_players, element_stats_df, element_types_df
    createEventsDataFrames()
    game_settings_full_dict = general_info_json.get('game_settings')
    phases_df = pd.DataFrame(general_info_json['phases'])
    createTeamsDataFrames()
    total_players = general_info_json.get('total_players')
    createElementsDataFrames
    element_stats_df = pd.DataFrame(general_info_json['element_stats'])
    element_types_df = pd.DataFrame(general_info_json['element_types'])

def createEventsDataFrames():
    global events_df, events_general_info_df, previous_event_int, current_event_int, next_event_int, events_deadline_df, events_user_scored_df, events_user_management_df
    events_df = pd.DataFrame(general_info_json['events'])
    events_general_info_df = events_df[['id', 'name', 'is_previous', 'is_current', 'is_next', 'finished', 'data_checked']]
    previous_event_int = events_general_info_df[events_general_info_df.is_previous == True].get('id')
    current_event_int = events_general_info_df[events_general_info_df.is_current == True].get('id')
    next_event_int = events_general_info_df[events_general_info_df.is_next == True].get('id')
    events_deadline_df = events_df[['id', 'deadline_time', 'deadline_time_epoch', 'deadline_time_game_offset']]
    events_user_scored_df = events_df[['id', 'average_entry_score', 'highest_scoring_entry', 'highest_score']]
    events_user_management_df = events_df[['id', 'chip_plays', 'most_selected', 'most_transferred_in', 'top_element', 'top_element_info', 'transfers_made', 'most_captained', 'most_vice_captained']]

def createTeamsDataFrames():
    global teams_df, teams_results_df, teams_name_df, teams_short_name_df, teams_rating_df, teams_unavailable_df, teams_pulse_id_df
    teams_df = pd.DataFrame(general_info_json['teams'])
    teams_results_df = teams_df[['code', 'position', 'played', 'win', 'draw', 'loss', 'points']]
    teams_name_df = teams_df[['code', 'id', 'name', 'short_name']]
    teams_rating_df = teams_df[['code', 'strength', 'strength_attack_home', 'strength_defence_home', 'strength_overall_home', 'strength_attack_away', 'strength_defence_away', 'strength_overall_away']]
    teams_unavailable_df = teams_df[['code', 'unavailable']]
    teams_pulse_id_df = teams_df[['code', 'pulse_id']]

def createElementsDataFrames():
    global elements_df, player_id_df, player_team_position_df, player_cost_df, player_status_df, player_points_df, player_user_transfers_df, player_stats_df, player_value_df, player_ep_ict_df, player_set_piece_df, player_news_df, player_dreamteam_df, player_chance_of_playing_df, not_unavailable_elements_df, available_elements_df
    elements_df = pd.DataFrame(general_info_json['elements'])
    player_id_df = elements_df[['id', 'code', 'first_name', 'second_name', 'web_name', 'photo']]
    player_team_position_df = elements_df[['id', 'team_code', 'element_type']]
    #elements_df['start_cost'] = elements_df['now_cost'] - elements_df['cost_change_start_fall']
    player_cost_df = elements_df[['id', 'now_cost', 'cost_change_start', 'cost_change_start_fall', 'cost_change_event', 'cost_change_event_fall']]
    player_status_df = elements_df[['id', 'status']]
    player_points_df = elements_df[['id', 'event_points', 'total_points', 'bonus', 'bps']]
    player_user_transfers_df = elements_df[['id', 'transfers_in', 'transfers_in_event', 'transfers_out', 'transfers_out_event', 'selected_by_percent']]
    player_stats_df = elements_df[['id', 'minutes', 'goals_scored', 'assists', 'clean_sheets', 'goals_conceded', 'own_goals', 'penalties_saved', 'penalties_missed', 'yellow_cards', 'red_cards', 'saves']]
    player_value_df = elements_df[['id', 'value_form', 'value_season', 'points_per_game']]
    player_ep_ict_df = elements_df[['id', 'ep_this', 'ep_next', 'influence', 'influence_rank', 'creativity', 'creativity_rank', 'creativity_rank_type', 'threat', 'threat_rank', 'threat_rank_type', 'ict_index', 'ict_index_rank', 'ict_index_rank_type']]
    player_set_piece_df = elements_df[['id', 'team_code', 'corners_and_indirect_freekicks_order', 'direct_freekicks_order', 'penalties_order']]
    player_news_df = elements_df[['id', 'news', 'news_added']]
    player_dreamteam_df = elements_df[['id', 'dreamteam_count', 'in_dreamteam']]
    player_chance_of_playing_df = elements_df[['id', 'status', 'chance_of_playing_this_round', 'chance_of_playing_next_round']]
    not_unavailable_elements_df = elements_df[elements_df['status'].isin(['a', 'd', 'i', 's'])]
    available_elements_df = elements_df[elements_df['status'] == 'a']

def createFixturesDataFrame():
    global fixtures_df, fixtures_event_code_df, fixtures_timings_df, fixtures_teams_df, fixtures_scores_df, fixtures_difficulty_df
    fixtures_df = pd.DataFrame(fixtures_json)
    fixtures_event_code_df = fixtures_df[['id', 'code', 'event']]
    fixtures_timings_df = fixtures_df[['id', 'kickoff_time', 'minutes', 'started', 'finished', 'finished_provisional']]
    fixtures_teams_df = fixtures_df[['id', 'team_h', 'team_a']]
    fixtures_scores_df = fixtures_df[['id', 'team_h_score', 'team_a_score']]
    fixtures_difficulty_df = fixtures_df[['id', 'team_h_difficulty', 'team_a_difficulty']]

def getplayersHistoryDict():
    return fetchStoredData(appconstants.playersHistory)

def getPreviousSeasonPointsDf():
    playersHistoryDict = getplayersHistoryDict()
    past_player_codes = []
    past_player_points = []
    for element in playersHistoryDict:
        players_seasons = playersHistoryDict.get(element)
        if players_seasons != []:
            previous_season = players_seasons[len(players_seasons)-1]
            if previous_season.get('season_name') == '2020/21':
                past_player_codes.append(previous_season.get('element_code'))
                past_player_points.append(previous_season.get('total_points'))

    past_player_points_dict = {'past_player_codes':past_player_codes, 'past_player_points':past_player_points}
    return pd.DataFrame(past_player_points_dict)

def predictData():
    global players_df, gameweek_fixture_df, team_codes_df
    players_1617_df = pd.read_csv(appconstants.players_1617)
    players_1718_df = pd.read_csv(appconstants.players_1718)
    players_1819_df = pd.read_csv(appconstants.players_1819)
    players_1920_df = pd.read_csv(appconstants.players_1920)
    players_2021_df = pd.read_csv(appconstants.players_2021)
    players_2122_df = pd.read_csv(appconstants.players_2122)

    gameweek_fixture_1617_df = pd.read_csv(appconstants.gameweeks_1617)
    gameweek_fixture_1718_df = pd.read_csv(appconstants.gameweeks_1718,encoding='latin')
    gameweek_fixture_1819_df = pd.read_csv(appconstants.gameweeks_1819,encoding='latin')
    gameweek_fixture_1920_df = pd.read_csv(appconstants.gameweeks_1920,engine='python')
    gameweek_fixture_2021_df = pd.read_csv(appconstants.gameweeks_2021,engine='python')

    if live:
        fixtureHistoryDict = {}
        fixtureDict = {}
        for element in elements_df['id']:
            fixtureHistoryDict[element] = fetchData(appconstants.historyUrl.replace('{element_id}', str(element)), None).get('history')
            fixtureDict[element] = fetchData(appconstants.historyUrl.replace('{element_id}', str(element)), None).get('fixtures')

        allHistoryDfs = []
        for element, dicts in fixtureHistoryDict.items():
            dfs = []
            gwCount = 1
            for dict in dicts:
                temp = pd.DataFrame(dict, index=[0])
                temp['GW'] = gwCount
                gwCount += 1
                dfs.append(temp)
            allHistoryDfs.append(pd.concat(dfs))

        fixtureDict = {}
        for element in elements_df['id']:
            fixtureDict[element] = fetchData(appconstants.historyUrl.replace('{element_id}', str(element)), None).get('fixtures')
        allDfs = []
        for element, dicts in fixtureDict.items():
            dfs = []
            for dict in dicts:
                temp = pd.DataFrame(dict, index=[0])
                temp = temp.rename(columns={'event':'GW', 'is_home':'was_home', 'id':'fixture'})
                temp['element'] = element
                temp['opponent_team'] = temp.apply(lambda x: getOpponentTeam(x.was_home, x.team_h, x.team_a), axis=1)
                temp = temp[['element', 'fixture', 'opponent_team', 'was_home', 'kickoff_time', 'team_h_score', 'team_a_score', 'GW']]
                dfs.append(temp)
            allDfs.append(pd.concat(dfs))

        history_df = pd.concat(allHistoryDfs)
        fixture_df = pd.concat(allDfs)

        for key in history_df.keys():
            if key not in fixture_df.keys():
                fixture_df[key] = 0

        gameweek_fixture_2122_df = pd.concat([history_df, fixture_df[fixture_df['GW'] == history_df.GW.max() + 1]])
    else:
        gameweek_fixture_2122_df = pd.read_csv(appconstants.gameweeks_2122,engine='python')
    
    team_codes_df = pd.read_csv(appconstants.team_codes)

    player_df_list = [players_1617_df, players_1718_df, players_1819_df, players_1920_df, players_2021_df, players_2122_df]
    gw_df_list = [gameweek_fixture_1617_df, gameweek_fixture_1718_df, gameweek_fixture_1819_df, gameweek_fixture_1920_df, gameweek_fixture_2021_df, gameweek_fixture_2122_df]

    seasons = ['1617', '1718', '1819', '1920', '2021', '2122']
    season_nums = list(range(len(seasons)))

    for i in range(len(seasons)):
        player_df_list[i]['season'] = seasons[i]
        gw_df_list[i]['season'] = seasons[i]
        player_df_list[i]['season_num'] = season_nums[i]
        gw_df_list[i]['season_num'] = season_nums[i]

    if live:
        gameweek_fixture_2122_df['name'] = gameweek_fixture_2122_df.element.map(elements_df.set_index('id').first_name) + ' ' + gameweek_fixture_2122_df.element.map(elements_df.set_index('id').second_name)
        gameweek_fixture_2122_df['team'] = gameweek_fixture_2122_df.element.map(elements_df.set_index('id').team_code).map(team_codes_df[team_codes_df['season'] == appconstants.CURRENT_SEASON].set_index('team_code').name)

        manipulation.dropColumnByName(gameweek_fixture_2122_df, 'element')

    players_df = pd.concat(player_df_list)
    players_df.reset_index(inplace=True)
    gameweek_fixture_df = pd.concat(gw_df_list)
    gameweek_fixture_df.reset_index(inplace=True)

    if live:
        gameweek_fixture_df = gameweek_fixture_df.astype({'influence': 'float64'})
        gameweek_fixture_df = gameweek_fixture_df.astype({'creativity': 'float64'})
        gameweek_fixture_df = gameweek_fixture_df.astype({'threat': 'float64'})
        gameweek_fixture_df = gameweek_fixture_df.astype({'ict_index': 'float64'})

    team_codes_df['season'] = team_codes_df.season.replace(team_codes_df.season.unique(), seasons)

def getOpponentTeam(home, team_h, team_a):
    if home:
        return team_h
    else:
        return team_a

def setListOfGameweeksPred(int):
    global prediction_gameweeks
    for i in range(1, int+1):
        prediction_gameweeks.append(i)
    storeJson(prediction_gameweeks, appconstants.predListOfGameweeksJsonDir)

# Manager Data functions

def setListOfGameweeks():
    global manager_gameweeks
    for event in events_df['id']:
        try:
            gameweekPicks = fetchData(appconstants.managerTeamPerGameweekUrl.replace('{manager_id}', manager_security_json.get('id')).replace('{event_id}', str(event)), None).get('picks')
            if gameweekPicks != None:
                manager_gameweeks.append(event)
        except:
            break
    storeJson(manager_gameweeks, appconstants.managerListOfGameweeksJsonDir)

def getManagerData():
    global manager_security_json, manager_basic_info_json, manager_history_json

    manager_security_json = fetchStoredData(appconstants.managerSecurityDir)

    if manager_security_json.get('id') != None:
        manager_basic_info_json = fetchData(appconstants.managerBasicInfoUrl.replace('{manager_id}', manager_security_json.get('id')), None)
        manager_history_json = fetchData(appconstants.managerHistoryUrl.replace('{manager_id}', manager_security_json.get('id')), None)
        setListOfGameweeks()
    else:
        print('Error: Cannot refresh data')

def getGameweekTeamData(event_id):
    gameweek_picks_json = fetchData(appconstants.managerTeamPerGameweekUrl.replace('{manager_id}', manager_security_json.get('id')).replace('{event_id}', event_id), None)
    return pd.DataFrame(gameweek_picks_json['picks'])

def getPlayerGameweekData(event_id):
    gameweek_live_json = fetchData(appconstants.eventUrl.replace('{event_id}', str(event_id)), None)
    return gameweek_live_json.get('elements')