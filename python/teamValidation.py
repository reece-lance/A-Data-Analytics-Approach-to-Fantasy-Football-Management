import data

budget = 1000
MAX_PLAYERS_PER_CLUB = 3
COUNT_PER_POSITION = {1: 2, 2: 5, 3: 5, 4: 3}

def validate(team):
    teamToCheck = team[['id']]
    return {'positions' : validatePositions(teamToCheck), 'teams' : validateClubs(teamToCheck), 'cost' : validateCost(teamToCheck)}

def validateCost(team): # checks if cost is over £100M
    try:
        if sum(team.id.map(data.elements_df.set_index('id').start_cost)) > budget:
            return False
        return True
    except:
        return False

def validateClubs(team): # checks there is no more than 3 players from each club
    try:
        team['temp_club'] = team.id.map(data.elements_df.set_index('id').team_code)
        if max(team.groupby('temp_club').count()['id'].to_dict().values()) > MAX_PLAYERS_PER_CLUB:
            team = team.drop(columns=['temp_club'])
            return False
        team = team.drop(columns=['temp_club'])
        return True
    except:
        return False
    
def validatePositions(team): # checks there is the correct amount of players per position
    try:
        team['temp_pos'] = team.id.map(data.elements_df.set_index('id').element_type)
        for pos, count in team.groupby('temp_pos').count()['id'].to_dict().items():
            if count != COUNT_PER_POSITION.get(pos):
                team = team.drop(columns=['temp_pos'])
                return False
        team = team.drop(columns=['temp_pos'])
        return True
    except:
        return False