import data
import appconstants

def leagueTableJson():
    league_table_df = data.teams_df[['position', 'badge', 'id', 'played', 'win', 'draw', 'loss', 'goals_for', 'goals_against', 'goal_difference', 'points']].sort_values(by=['points', 'goal_difference', 'goals_for'], ascending=False, ignore_index=True)
    league_table_df['id'] = league_table_df.id.map(data.teams_df.set_index('id').name)
    league_table_df = league_table_df.rename(columns={"id": "team"})
    league_table_df.to_json(appconstants.leagueTableDir, orient='records')