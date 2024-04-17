import data
import appconstants

def resultsTableJson():
    results_df = data.fixtures_df[['kickoff_time','team_h', 'team_h_score', 'team_a_score', 'team_a']]
    results_df = results_df[data.fixtures_df['minutes'] != 0]
    results_df['badge_h'] = results_df.team_h.map(data.teams_df.set_index('id').badge)
    results_df['badge_a'] = results_df.team_a.map(data.teams_df.set_index('id').badge)
    results_df['team_h'] = results_df.team_h.map(data.teams_df.set_index('id').name)
    results_df['team_a'] = results_df.team_a.map(data.teams_df.set_index('id').name)
    results_df[['date','time']] = results_df['kickoff_time'].str.split('T',expand=True)
    results_df['time'] = results_df['time'].str[:-4]

    for index, row in results_df.iterrows():
        results_df.at[index, 'score'] = str(int(row['team_h_score'])) + " - " + str(int(row['team_a_score']))

    results_df = results_df[['date', 'time', 'team_h', 'badge_h', 'score', 'badge_a', 'team_a']]

    results_df.iloc[::-1].to_json(appconstants.resultsTableDir, orient='records')