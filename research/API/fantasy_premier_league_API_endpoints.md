Fantasy Premier League API

All data is found at: https://fantasy.premierleague.com/

General Information:

Endpoint path: bootstrap-static/
URL: https://fantasy.premierleague.com/api/bootstrap-static/

* events: Basic information of every Gameweek such as average score, highest score, top scoring player, most captained, etc.

* game_settings: The game settings and rules. (not important)

* phases: Phases of FPL season. (not really important)

* teams: Basic information of current Premier League clubs.

* total_players: Total FPL players.

* elements: Information of all Premier League players including points, status, value, match stats (goals, assists, etc.), ICT index, etc.

* element_types: Basic information about player’s position (GK, DEF, MID, FWD).

Fixtures:

Endpoint path: fixtures/
URL: https://fantasy.premierleague.com/api/fixtures/

* event: refers to the event id in events section of the bootstrap-static data.

* team_a and team_h: refers to the team id in teams section of the bootstrap-static data. team_a for the away team and team_h for the home team.

* team_h_difficulty and team_a_difficulty: is the FDR value calculated by FPL.

* stats: contains a list of match facts that affect points of a player. It consists of goals_scored, assists, own_goals, penalties_saved, penalties_missed, yellow_cards, red_cards, saves, bonus, and bps data.
* value: is the amount

* element: refers to the element id

Player’s Detailed Data

Endpoint path: element-summary/{element_id}/
URL: https://fantasy.premierleague.com/api/element-summary/{element_id}/

* fixtures: A list of player’s remaining fixtures of the season. Each fixture object consists of these information below:

* history: A list of player’s previous fixtures and its match stats.

* history_past: A list of player’s previous seasons and its seasonal stats.

Gameweek Live Data

Endpoint path: event/{event_id}/live/
URL: https://fantasy.premierleague.com/api/event/{event_id}/live/

* id: Refers to the element id in elements section of the bootstrap-static data.

* stats: Player’s match stats including goals, assists, etc.

* explain: Breakdown of a player’s event points.


Source: https://medium.com/@frenzelts/fantasy-premier-league-api-endpoints-a-detailed-guide-acbd5598eb19 on 30-09-21