##Handels the tests for robustness of the program
import os
import sys
import pytest
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from House.house import *
from Queries.read import selectSingle

##Tests the case where elevations is called on a house that is not in the database
##      Expectes an InvalidHouseExcetion
def test_elevationsHouseDoesntExist():
    try:
        testHouse = House("DNE",-1,-1,[],[],[],[],[])
        testHouse.elevations()
        pytest.fail("Test Failed: Exception should have been thrown")
    except InvalidHouseException:
        assert True
    except Exception as e:
        print(e)
        pytest.fail("Test Failed: Did not catch the correct exception")


##Tests the case where models is called on a house that is not in the database
def test_modelsHouseDoesntExist():
    try:
        testHouse = House("DNE",-1,-1,[],[],[],[],[])
        testHouse.models()
        pytest.fail("Test Failed: Exception should have been thrown")
    except InvalidHouseException:
        assert True
    except Exception as e:
        print(e)
        pytest.fail("Test Failed: Did not catch the correct exception")

##Tests the case where colours is called on a house that is not in the database
def test_coloursHouseDoesntExist():
    try:
        testHouse = House("DNE",-1,-1,[],[],[],[],[])
        testHouse.colours()
        pytest.fail("Test Failed: Exception should have been thrown")
    except InvalidHouseException:
        assert True
    except Exception as e:
        print(e)
        pytest.fail("Test Failed: Did not catch the correct exception")