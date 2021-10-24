import pandas as pd
import appconstants
from api import fetchData

# JSON data
general_info_json = fixtures_json = None

# GENERAL INFO
# Events
events_df = events_general_info_df = events_deadline_df = events_user_scored_df = events_user_management_df = None
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
# Element Stats
element_stats_df = None
# Element Types
element_types_df = None

# FIXTURES
fixtures_df = fixtures_event_code_df = fixtures_timings_df = fixtures_teams_df = fixtures_scores_df = fixtures_difficulty_df = None

# CUSTOM
team_fdr = None

def refreshData():
    global general_info_json, fixtures_json
    general_info_json = fetchData('https://fantasy.premierleague.com/api/bootstrap-static/', appconstants.generalInfoJsonDir)
    fixtures_json = fetchData('https://fantasy.premierleague.com/api/fixtures/', appconstants.fixturesJsonDir)
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
    global events_df, events_general_info_df, events_deadline_df, events_user_scored_df, events_user_management_df
    events_df = pd.DataFrame(general_info_json['events'])
    events_general_info_df = events_df[['id', 'name', 'is_previous', 'is_current', 'is_next', 'finished', 'data_checked']]
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
    global elements_df, player_id_df, player_team_position_df, player_cost_df, player_status_df, player_points_df, player_user_transfers_df, player_stats_df, player_value_df, player_ep_ict_df, player_set_piece_df, player_news_df, player_dreamteam_df, player_chance_of_playing_df
    elements_df = pd.DataFrame(general_info_json['elements'])
    player_id_df = elements_df[['id', 'code', 'first_name', 'second_name', 'web_name', 'photo']]
    player_team_position_df = elements_df[['id', 'team_code', 'element_type']]
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

def createFixturesDataFrame():
    global fixtures_df, fixtures_event_code_df, fixtures_timings_df, fixtures_teams_df, fixtures_scores_df, fixtures_difficulty_df
    fixtures_df = pd.DataFrame(fixtures_json)
    fixtures_event_code_df = fixtures_df[['id', 'code', 'event']]
    fixtures_timings_df = fixtures_df[['id', 'kickoff_time', 'minutes', 'started', 'finished', 'finished_provisional']]
    fixtures_teams_df = fixtures_df[['id', 'team_h', 'team_a']]
    fixtures_scores_df = fixtures_df[['id', 'team_h_score', 'team_a_score']]
    fixtures_difficulty_df = fixtures_df[['id', 'team_h_difficulty', 'team_a_difficulty']]