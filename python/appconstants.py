import os

absolutepath = os.path.abspath(__file__)

fileDir = os.path.dirname(absolutepath)

parentDir = os.path.dirname(fileDir)

storedDataPath = os.path.join(fileDir, 'stored_data')

generalInfoJsonDir = os.path.join(storedDataPath, 'general-info.json')
fixturesJsonDir = os.path.join(storedDataPath, 'fixtures.json')

player_images_link_1 = 'https://resources.premierleague.com/premierleague/photos/players/110x140/p'
# element code
player_images_link_2 = '.png'