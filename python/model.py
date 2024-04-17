import pandas as pd
import data
import appconstants

def applyModel():
    getBestValueSeason()
    getBestValueSeason().to_json(appconstants.bvsjsonDir, orient='records')

def getBestValueSeason():
    player_value_df_sorted = data.player_value_df[['id', 'value_season']].sort_values(by=['value_season'], ascending=False, ignore_index=True)
    top_15_inform_players_df = player_value_df_sorted[['id']][:15]
    top_15_inform_players_df['first_name'] = top_15_inform_players_df.id.map(data.player_id_df.set_index('id').first_name)
    top_15_inform_players_df['second_name'] = top_15_inform_players_df.id.map(data.player_id_df.set_index('id').second_name)

    return top_15_inform_players_df