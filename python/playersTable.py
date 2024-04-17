import data
import appconstants

def playersTableJson():
    players_df = data.elements_df[['second_name', 'team', 'element_type', 'now_cost', 'selected_by_percent', 'form', 'total_points']]
    players_df['team'] = players_df.team.map(data.teams_df.set_index('id').name)
    players_df['element_type'] = players_df.element_type.map(data.element_types_df.set_index('id').singular_name)
    players_df['now_cost'] = players_df['now_cost'] / 10

    players_df.to_json(appconstants.playersTableDir, orient='records')