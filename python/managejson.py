import json

# fetches locally stored data from json file
def fetchStoredData(fileName):
    file = open(fileName)
    return json.load(file) # returns json data

# stores data locally in json file
def storeData(data, fileName):
    file = open(fileName, "w") # opens file and prepares to write
    file.write(json.dumps(data)) # writes json data to json file
    file.close()