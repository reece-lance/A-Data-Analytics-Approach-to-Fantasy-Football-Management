import json

# fetches locally stored data from json file
def fetchStoredData(fileName):
    try:
        file = open(fileName)
        return json.load(file) # returns json data
    except:
        return {}

# stores data locally in json file
def storeJson(data, fileDir):
    writeToFile(json.dumps(data), fileDir) # converts data to json type and writes to file

# stores data locally at file directory
def writeToFile(data, fileDir):
    file = open(fileDir, "w") # opens file and prepares to write
    file.write(data) # writes data to file
    file.close() # cloces file