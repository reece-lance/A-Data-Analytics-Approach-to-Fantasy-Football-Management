import data
from data import getGameweekTeamData
from datapreprocessing import createTeam

def createTeamsPerGameweek():
    for event in data.manager_gameweeks:
        gameweek_picks_df = getGameweekTeamData(str(event))
        print(gameweek_picks_df)
        gameweek_picks_df = createTeam(gameweek_picks_df, event)
        data.manager_team_dict[event] = gameweek_picks_df