import os

CURRENT_SEASON = '2122'
LAST_SEASON = '2021'

absolutepath = os.path.abspath(__file__)

fileDir = os.path.dirname(absolutepath)

parentDir = os.path.dirname(fileDir)

mainFinished = os.path.join(fileDir, 'mainFinished.json')

signInFinished = os.path.join(fileDir, 'signInFinished.json')

storedDataPath = os.path.join(fileDir, 'stored_data')

playersHistory = os.path.join(fileDir, 'players_history.json')
historyUrl = 'https://fantasy.premierleague.com/api/element-summary/{element_id}/'

generalInfoUrl = 'https://fantasy.premierleague.com/api/bootstrap-static/'
fixturesUrl = 'https://fantasy.premierleague.com/api/fixtures/'
eventUrl = 'https://fantasy.premierleague.com/api/event/{event_id}/live/'

generalInfoJsonDir = os.path.join(storedDataPath, 'general-info.json')
fixturesJsonDir = os.path.join(storedDataPath, 'fixtures.json')

teamsPath = os.path.join(fileDir, 'teams')

bvsjsonDir = os.path.join(teamsPath, 'best_value_season_team.json')

tablesPath = os.path.join(fileDir, 'tables')

playersTableDir = os.path.join(tablesPath, 'playersTable.json')
leagueTableDir = os.path.join(tablesPath, 'leagueTable.json')
resultsTableDir = os.path.join(tablesPath, 'resultsTable.json')
fixtureTableDir = os.path.join(tablesPath, 'fixtureTable.json')

badgesPath = os.path.join(fileDir, 'badges')

player_images_link_1 = 'https://resources.premierleague.com/premierleague/photos/players/110x140/p'
# element code
player_images_link_2 = '.png'

signInDataPath = os.path.join(storedDataPath, 'signInData')
predictionsPath = os.path.join(storedDataPath, 'predictions')

managerSecurityDir = os.path.join(signInDataPath, 'manager-security.json')

managerBasicInfoJsonDir = os.path.join(signInDataPath, 'manager-basic-info.json')
predBasicInfoJsonDir = os.path.join(predictionsPath, 'manager-basic-info.json')

managerListOfGameweeksJsonDir = os.path.join(signInDataPath, 'list-of-gameweeks.json')
predListOfGameweeksJsonDir = os.path.join(predictionsPath, 'list-of-gameweeks.json')

managerHistoryPath = os.path.join(signInDataPath, 'history')
managerHistoryJsonDir = os.path.join(managerHistoryPath, 'gameweek-{event_id}.json')

predHistoryPath = os.path.join(predictionsPath, 'history')
predHistoryJsonDir = os.path.join(predHistoryPath, 'gameweek-{event_id}.json')

managerTeamsPath = os.path.join(signInDataPath, 'teams')
managerTeamPerGameweekJsonDir = os.path.join(managerTeamsPath, 'gameweek-{event_id}.json')

predTeamsPath = os.path.join(predictionsPath, 'teams')
predTeamPerGameweekJsonDir = os.path.join(predTeamsPath, 'gameweek-{event_id}.json')

managerBasicInfoUrl = 'https://fantasy.premierleague.com/api/entry/{manager_id}/'
managerHistoryUrl = 'https://fantasy.premierleague.com/api/entry/{manager_id}/history/'
managerTeamPerGameweekUrl = 'https://fantasy.premierleague.com/api/entry/{manager_id}/event/{event_id}/picks/'

fpl_data_path = fileDir + '/fpldata/'

players_1617 = fpl_data_path + '16-17/players.csv'
players_1718 = fpl_data_path + '17-18/players.csv'
players_1819 = fpl_data_path + '18-19/players.csv'
players_1920 = fpl_data_path + '19-20/players.csv'
players_2021 = fpl_data_path + '20-21/players.csv'
players_2122 = fpl_data_path + '21-22/players.csv'

gameweeks_1617 = fpl_data_path + '16-17/gameweeks.csv'
gameweeks_1718 = fpl_data_path + '17-18/gameweeks.csv'
gameweeks_1819 = fpl_data_path + '18-19/gameweeks.csv'
gameweeks_1920 = fpl_data_path + '19-20/gameweeks.csv'
gameweeks_2021 = fpl_data_path + '20-21/gameweeks.csv'
gameweeks_2122 = fpl_data_path + '21-22/gameweeks.csv'

team_codes = fpl_data_path + 'teams.csv'