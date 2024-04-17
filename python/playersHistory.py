import appconstants
import data
import json
from api import fetchData
from datapreprocessing import preprocess

if __name__ == "__main__":
    preprocess()
    historyDict = {}
    for element in data.elements_df['id']:
        historyDict[element] = fetchData(appconstants.historyUrl.replace('{element_id}', str(element)), None).get('history_past')

    file = open(appconstants.playersHistory, "w")
    file.write(json.dumps(historyDict))
    file.close()