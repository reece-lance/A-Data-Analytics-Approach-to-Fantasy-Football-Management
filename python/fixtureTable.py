import appconstants
from datapreprocessing import createFixturesDf
import data

def fixtureTableJson():
    data.upcoming_fixtures = createFixturesDf()
    data.upcoming_fixtures.to_json(appconstants.fixtureTableDir, orient='records')