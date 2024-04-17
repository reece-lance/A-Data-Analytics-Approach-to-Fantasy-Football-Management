from datapreprocessing import preprocess
from datapreprocessing import createMyManagerData
from data import getManagerData
from teamsPerGameweek import createTeamsPerGameweek
from managejson import storeJson
from managejson import writeToFile
from manageFiles import replaceFolder
import appconstants
import data

if __name__ == "__main__":
    preprocess()
    getManagerData()
    createMyManagerData()
    createTeamsPerGameweek()

    storeJson(data.manager_basic_info_list, appconstants.managerBasicInfoJsonDir) # Writes manager basic info to file as json

    replaceFolder(appconstants.managerHistoryPath)
    replaceFolder(appconstants.managerTeamsPath)
    
    for event_id in data.manager_gameweeks:
        storeJson(data.manager_history_dict.get(event_id), appconstants.managerHistoryJsonDir.replace('{event_id}', str(event_id))) # Writes manager history to file as json
        data.manager_team_dict.get(event_id).to_json(appconstants.managerTeamPerGameweekJsonDir.replace('{event_id}', str(event_id)), orient='records') # Writes manager history to file as json

    writeToFile('true', appconstants.signInFinished) # Writes 'true' to file