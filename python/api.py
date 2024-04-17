import requests
from managejson import *

#Fetches the json data
def fetchData(url, fileName):
    try:
        r = requests.get(url) # response from the api
        data = r.json() # json data as dictionary
        if fileName != None:
            storeJson(data, fileName) # stores data locally in json file
        return data
    except:
        return fetchStoredData(fileName) # fetches locally stored data from json file