import os
import shutil

def replaceFolder(dir):
    deleteFolder(dir)
    createFolder(dir)

def createFolder(dir):
    os.mkdir(dir)

#https://mkyong.com/python/python-how-to-delete-a-file-or-folder/
def deleteFolder(dir):
    try:
        shutil.rmtree(dir)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))