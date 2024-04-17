import pandas as pd
from sklearn.linear_model import LinearRegression
import appconstants
import data
import datapreprocessing
import manipulation
import manageFiles
import pulp

def predict():
    initialTeam()
    createTestTrainData()
    createLRModel()
    teams, transfers = getPredictedStartingXI()
    print('\n*** Transfers ***\n')
    print(transfers)
    getTeams(teams)

    manageFiles.replaceFolder(appconstants.predTeamsPath)

    total_points_list = []
    print('\n*** Points per gameweek ***\n')
    for event_id in data.prediction_gameweeks:
        data.pred_team_dict.get(event_id).to_json(appconstants.predTeamPerGameweekJsonDir.replace('{event_id}', str(event_id)), orient='records') # Writes manager history to file as json
        gw_points = data.pred_team_dict.get(event_id).points.sum()

        print('Total points for gameweek', event_id, ':', gw_points)
        total_points_list.append(gw_points)

        transfer_details = transfers.iloc[event_id-1]

        if len(transfer_details.get('player_in')) > 0:
            transferAmount = 1
        else:
            transferAmount = 0
            
        text_file = open(appconstants.predHistoryJsonDir.replace('{event_id}', str(event_id)), "w")
        text_file.write('[{"keys": "Points", "values": '+ str(gw_points) + '}, {"keys": "Total Points", "values": ' + str(sum(total_points_list)) + '}, {"keys": "Rank", "values": "?"}, {"keys": "Transfers", "values": ' + str(transferAmount) + '}, {"keys": "Transfers Cost", "values": "\u00a3' + str(float(transfer_details.get('money_change'))) + 'M"}, {"keys": "Points On Bench", "values": ' + str(0) + '}]')
        text_file.close()
    
    print()
    print('Total points for season so far with transfers:', sum(total_points_list))

def getTeams(teams_df_list):
    data.setListOfGameweeksPred(len(teams_df_list))
    for event in data.prediction_gameweeks:
        gameweek_picks_df = getTeam(teams_df_list.get(event))
        gameweek_picks_df = datapreprocessing.createTeam(gameweek_picks_df, event)
        data.pred_team_dict[event] = gameweek_picks_df
        
def getTeam(team_df):
    team_df['multiplier'] = 1
    bench_df = pd.DataFrame(data={'full_name' : data.subs})
    bench_df['multiplier'] = 0
    team_df = pd.concat([team_df, bench_df])
    #team_df = team_df.reset_index(drop='index')
    team_df['position'] = team_df.full_name.map(data.player_positions.set_index('full_name').position).map({'Keeper' : 1, 'Defender': 2, 'Midfielder' : 3, 'Forward' : 4})
    team_df['prev_total_points'] = team_df.full_name.map(data.previous_season_player_df.set_index('full_name').total_points)
    manipulation.fillEmptyValueColumn(team_df, 0)
    team_df['is_captain'] = False
    team_df['is_vice_captain'] = False
    team_df.loc[team_df.full_name == team_df[team_df['position'] != 1].sort_values("prev_total_points", ascending=False).head(1).full_name.values[0], 'is_captain'] = True
    team_df.loc[team_df.full_name == team_df[team_df['is_captain'] == False].sort_values("prev_total_points", ascending=False).head(1).full_name.values[0], 'is_vice_captain'] = True
    team_df = team_df.sort_values(by=['multiplier', 'position'], ascending=[False, True])
    team_df = team_df.reset_index(drop='index')
    team_df['position'] = team_df.index + 1
    team_df.loc[team_df.is_captain == True, 'multiplier'] = 2
    players = data.elements_df[['id', 'first_name', 'second_name']]
    players['full_name'] = players.apply(lambda x: datapreprocessing.get_full_name_playerdf(x.first_name, x.second_name), axis=1).str.lower()
    team_df['element'] = team_df[['full_name']].replace(players.full_name.values, players.id.values)
    return team_df[['element', 'position', 'multiplier', 'is_captain', 'is_vice_captain']]

# The rest of this code was written using https://www.kaggle.com/code/gavinjpng/fpl-prediction-and-selection/notebook as reference. Some methods copied in order to have the prediction work efficiently. I have zero intention of plagarism.

def initialTeam():
    data.subs, data.subs_cost = get_bench_players(data.available_players_df)
    budget = 1000 - data.subs_cost
    lp = SolveLP(budget)
    data.initial_team_df = get_initial_team(lp, data.available_players_df)
    captain = get_initial_team(lp, data.previous_season_player_df).sort_values("total_points", ascending=False).head(1).full_name.values[0]
    total_points = data.current_season_player_df[data.current_season_player_df.full_name.isin(data.initial_team_df.full_name)].total_points.sum()
    total_points += data.current_season_player_df[data.current_season_player_df.full_name == captain].total_points
    total_points = getTeamScore(lp)

    print('\n*** Initial Team ***\n')
    print(data.initial_team_df[['full_name', 'position', 'now_cost', 'player_team_name', 'total_points']])
    print("Total points for", appconstants.CURRENT_SEASON[:2] + '-' + appconstants.CURRENT_SEASON[2:], "season based off initial team only:", total_points.values[0])
    print()

    return data.subs

def getTeamScore(lp):
    captain = get_initial_team(lp, data.previous_season_player_df).sort_values("total_points", ascending=False).head(1).full_name.values[0]
    total_points = data.current_season_player_df[data.current_season_player_df.full_name.isin(data.initial_team_df.full_name)].total_points.sum()
    return total_points + data.current_season_player_df[data.current_season_player_df.full_name == captain].total_points

def SolveLP(budget):
    starting_available_players = data.available_players_df[data.available_players_df.status == 'a']
    starting_available_players = starting_available_players.reset_index(drop='index')
    lp = pulp.LpProblem('StartingXI', pulp.LpMaximize)
    options = get_options(starting_available_players)
    lp += total_points_restriction(starting_available_players, options)
    lp += budget_restriction(starting_available_players, options, budget)
    pos = ['Keeper', 'Defender', 'Midfielder', 'Forward']
    amount = [1, 4, 4, 2]
    for i in range(4):
        lp +=  position_restriction(pos[i], amount[i], options, starting_available_players)
    team_restriction(lp, starting_available_players, options)

    lp.writeLP('StartingXI.lp')
    lp.solve()

    return lp

def createCumvariables():
    player_variables_to_cum = ['assists', 'bonus', 'bps', 'creativity', 'clean_sheets', 'goals_conceded', 'goals_scored', 'ict_index', 'influence', 'minutes', 'threat']
    team_variables_to_cum = ['goals_conceded', 'goals_scored', 'team_points', 'opponent_points']

    cumulative_gw_fix_df_players, cumulative_player_variables = player_cum_variables(data.gameweek_fixture_df, player_variables_to_cum, ['all', 1, 3, 5])
    data.cumulative_gw_fix_df, cumulative_team_variables = team_cum_variables(cumulative_gw_fix_df_players, team_variables_to_cum, ['all', 1, 3, 5])

    data.relevant_variables = ['position', 'was_home', 'minutes', 'value', 'round', 'season_num'] + cumulative_player_variables + cumulative_team_variables
    data.categorical_variables = ['was_home', 'position']
    data.numerical_variables = data.numerical_variables = list(set(data.relevant_variables) - set(data.categorical_variables))

    for feat in ['position', 'last_all_goals_conceded_team', 'opponent_last_all_goals_conceded', 'last_1_goals_conceded_team', 'opponent_last_1_goals_conceded', 'last_3_goals_conceded_team', 'opponent_last_3_goals_conceded', 'last_5_goals_conceded_team', 'opponent_last_5_goals_conceded']:
        if feat in data.relevant_variables:
            data.relevant_variables.remove(feat)
        if feat in data.numerical_variables:
            data.numerical_variables.remove(feat)
        if feat in data.categorical_variables:
            data.categorical_variables.remove(feat)

def createTestTrainData():
    createCumvariables()
    train_df = data.cumulative_gw_fix_df[(data.cumulative_gw_fix_df.season != appconstants.CURRENT_SEASON)]
    data.test_df = data.cumulative_gw_fix_df[(data.cumulative_gw_fix_df.season == appconstants.CURRENT_SEASON)]

    data.X_train = pd.concat([train_df[data.relevant_variables][data.numerical_variables], pd.get_dummies(train_df[data.relevant_variables][data.categorical_variables].astype(str))], axis=1)
    data.y_train = train_df.total_points

    data.X_test = pd.concat([data.test_df[data.numerical_variables], pd.get_dummies(data.test_df[data.categorical_variables].astype(str))], axis=1)
    data.y_test = data.test_df.total_points

def createLRModel():
    lin_reg = LinearRegression()
    lin_reg.fit(data.X_train, data.y_train)
    linreg_predictions = lin_reg.predict(data.X_test)
    data.test_df['position'] = data.test_df.full_name.map(data.player_positions.set_index('full_name').position)
    data.pred_df_lin_reg = make_predicted_table(data.y_test, linreg_predictions, data.test_df[data.relevant_variables + ['full_name', 'GW', 'player_team_name', 'total_points', 'position']])

def getPredictedStartingXI():
    my_team = list(data.initial_team_df.full_name)
    gameweeks = (data.test_df.GW).unique()
    starting_money = 1000 - data.subs_cost - data.initial_team_df.starting_cost.sum()
    return get_performance(my_team, starting_money, gameweeks, data.pred_df_lin_reg)

def get_bench_players(player_df):
    bench_player_names = []
    cost = 0

    for position, players in player_df.groupby('position'):
        cheapest_players =  players[(players.starting_cost == players.starting_cost.min())]
        bench_player = cheapest_players[cheapest_players.total_points == cheapest_players.total_points.max()]
        bench_player_name = bench_player.full_name.values[0]
        cost += bench_player.starting_cost.values[0]
        bench_player_names += [bench_player_name]

    return bench_player_names, cost

def get_options(player_df):
    return [pulp.LpVariable(i, cat="Binary") for i in player_df.full_name]

def  total_points_restriction(player_df, options):
    total_tp = ""

    for i, player in enumerate(options):
        total_tp += player_df.prev_total_points[i] * player
        
    return total_tp

def budget_restriction(player_df, options, budget):
    total_paid = ""
    for rownum, row in player_df.iterrows():
        for i, player in enumerate(options):
            if rownum == i:
                formula = row['starting_cost'] * player
                total_paid += formula

    return (total_paid <= budget)

def position_restriction(position, n, options, player_df):
    total_n = ""
    player_positions = player_df.position
    
    for i, player in enumerate(options):
        if player_positions[i] == position:
            total_n += 1 * player
            
    return(total_n == n)

def team_restriction(prob, player_df, options):
    for team, group in player_df.groupby('team_code'):
        team_total = ''
        
        for player in options:
            if player.name in group.full_name.values:
                team_total += 1 * player
                
        prob += (team_total <= 3)

def get_initial_team(prob, player_df):
    variable_names = [v.name for v in prob.variables()]
    variable_values = [v.varValue for v in prob.variables()]

    initial_team = pd.merge(pd.DataFrame({'full_name': variable_names, 'chosen': variable_values}), player_df, on="full_name")
    
    initial_team = initial_team[initial_team.chosen==1.0] 
    
    return initial_team

def player_cum_variables(gameweek_fixture_df, variables, vars):
    out_df = gameweek_fixture_df.copy()
    cumulative_variables = []
    for variable in variables:
        for var in vars:
            cumulative_variable = 'last_' + str(var) + '_' + variable
            if var == 'all':
                out_df[cumulative_variable] = out_df.sort_values('round').groupby(['season', 'full_name'])[variable].apply(lambda x: x.cumsum() - x)
            else:
                out_df[cumulative_variable] = out_df.sort_values('round').groupby(['season', 'full_name'])[variable].apply(lambda x: x.rolling(min_periods = 1, window = var + 1).sum() - x)
            cumulative_variables.append(cumulative_variable)

    return out_df, cumulative_variables

def team_cum_variables(in_df, variables, vars):
    out_df = in_df.copy()
    cumulative_variables = []
    for variable in variables:
        variable_name = variable + '_team'
        opponent_variable_name = variable_name + '_opponent'
        variable_team = out_df.groupby(['player_team_name', 'season', 'round', 'kickoff_time', 'opponent_team_name'])[variable].max().rename(variable_name).reset_index()
        variable_team = variable_team.merge(variable_team, left_on=['player_team_name', 'season', 'round', 'kickoff_time', 'opponent_team_name'], right_on=['opponent_team_name', 'season', 'round', 'kickoff_time', 'player_team_name'], how='left', suffixes=('', '_opponent'))
        for var in vars:
            if var == 'all':
                variable_team['last_' + str(var) + '_' + variable_name] = variable_team.sort_values('round').groupby('player_team_name')[variable_name].apply(lambda x: x.cumsum() - x)
                variable_team['opponent_last_' + str(var) + '_' + variable] = variable_team.groupby('player_team_name')[opponent_variable_name].apply(lambda x: x.cumsum() - x)
            else:
                variable_team['last_' + str(var) + '_' + variable_name] = variable_team.sort_values('round').groupby('player_team_name')[variable_name].apply(lambda x: x.rolling(min_periods=1, window=var+1).sum()-x)
                variable_team['opponent_last_' + str(var) + '_' + variable] = variable_team.groupby('player_team_name')[opponent_variable_name].apply(lambda x: x.rolling(min_periods=1, window=var+1).sum()-x)
            cumulative_variables.extend(['last_' + str(var) + '_' + variable_name, 'opponent_last_' + str(var) + '_' + variable])
        out_df = out_df.merge(variable_team, on=['player_team_name', 'season', 'round', 'kickoff_time', 'opponent_team_name'], how='left')

        return out_df, cumulative_variables

def make_predicted_table(y_test, y_pred, df):
    results_df = pd.DataFrame(list(zip(y_test.tolist(), y_pred.tolist())), columns=["actual", "predicted"])
    results_df.reset_index(drop=True, inplace=True)
    df.reset_index(inplace=True)
    pred_df = pd.concat([df, results_df], axis=1)
    
    return pred_df

def get_suggested_transfer(pred_df, team_list, budget):
    pred_diff = 0
    money_change = 0
    pot_in = ''
    pot_out = ''
    team_df = pred_df[(pred_df.full_name.isin(team_list))]

    teams_dict = {}
    for i, row in team_df.iterrows():
        if row.player_team_name not in teams_dict:
            teams_dict[row.player_team_name] = [row.full_name]
        else:
            teams_dict[row.player_team_name].append(row.full_name)
            
    for pos in ["Defender", "Midfielder", "Forward"]:
        player_df = pred_df[pred_df.position == pos].sort_values('predicted', ascending=False).reset_index()
        lowest_pos = 0
        player_names = team_df[team_df.position == pos].full_name.values
        for p in player_names:
            player_pos = player_df[player_df.full_name == p].index[0]
            if player_pos > lowest_pos:
                lowest_pos = player_pos
                potential_out = p
                potential_out_cost = team_df[team_df.full_name == p].value.values[0]
                potential_out_team = team_df[team_df.full_name == p].player_team_name.values[0]
                
            elif len(player_names) <= 1:
                potential_out_cost = 0
                potential_out_team = 'none'
                potential_out = 'none'
                
        potential_players = player_df[:lowest_pos]
        
        try:
            potential_players = potential_players[potential_players.value <= potential_out_cost + budget] #only keep players within budget
            potential_players = potential_players[potential_players.minutes > 0] #only keep players who played
            potential_out_predicted = team_df[team_df.full_name == p].predicted.values[0] #choose the player who will make the most difference
            for i, row in potential_players.iterrows():
                if row.full_name in team_list:
                    continue
                if row.player_team_name not in teams_dict:
                    pass
                else:
                    if len(teams_dict[row.player_team_name]) == 3:
                        if row.player_team_name == potential_out_team:
                            pass
                        else:
                            continue
                    else:
                        pass

                # check for difference in predictions
                if row.predicted - potential_out_predicted > pred_diff:
                    pred_diff = row.predicted - potential_out_predicted
                    pot_in = row.full_name
                    pot_out = potential_out
                    money_change = potential_out_cost - row.value
        except:
            continue
                
    return pot_in, pot_out, money_change

def get_performance(team_list, starting_money, gameweek_fixture_list, prediction_df):
    current_money = starting_money
    teams = {}
    in_list = []
    out_list = []
    money_change_list = []

    for gw in gameweek_fixture_list:
        gameweek_fixture_df = prediction_df[prediction_df.GW==gw]
        money_change = 0
        pot_in = ''
        pot_out = ''

        if gw > 1:
            pot_in, pot_out, money_change = get_suggested_transfer(gameweek_fixture_df, team_list, current_money)
            current_money += money_change
            team_list.append(pot_in)
            team_list.remove(pot_out)

        out_list.append(pot_out)
        in_list.append(pot_in)
        money_change_list.append(money_change)
        teams[gw] = pd.DataFrame(data={'full_name' : team_list})

    transfers = pd.DataFrame({'GW': gameweek_fixture_list,
                          'player_in': in_list,
                          'player_out': out_list,
                          'money_change': [x / 10 for x in money_change_list]})
    
    return teams, transfers