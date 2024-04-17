from appconstants import mainFinished
from datapreprocessing import preprocess
from managejson import writeToFile
from prediction import predict
from playersTable import playersTableJson
from leagueTable import leagueTableJson
from resultsTable import resultsTableJson
from fixtureTable import fixtureTableJson

if __name__ == "__main__":
    preprocess()
    predict()
    playersTableJson()
    leagueTableJson()
    resultsTableJson()
    fixtureTableJson()
    writeToFile('true', mainFinished) # Writes 'true' to file