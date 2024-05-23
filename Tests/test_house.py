##Note To LIAM, you can run tests just by typing pytest when in the Tests directory
import os
import sys
import pytest

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from House.house import *

n = "Ryan"

def test_simple():
    assert 1 + 1 == 2

##Houses across have CL and PR elevations
def test_Elevation3AcrossMix():
    cross = [(n,1,1),(n,1,2),(n,1,3)]
    opp = House(n,1,4,cross,[],[],[],[])
    assert opp.elevations() == ["CR"]


#All 3 houses across have CL elevation
def test_Elevation3AcrossSame():
    cross = [(n,2,5),(n,2,6),(n,2,7)]
    opp = House(n,2,8,cross,[],[],[],[])
    assert sorted(opp.elevations()) == sorted(["CR","PR"])


##All 3 houses across have different elevation, expect empty return
def test_Elevation3AcrossAll():
    cross = [(n,3,9),(n,3,10),(n,3,11)]
    opp = House(n,3,12,cross,[],[],[],[])
    assert opp.elevations() == []

##All 3 houses across have no set elevation
def test_Elevation3AcrossEmpty():
    cross = [(n,4,13),(n,4,14),(n,4,15)]
    opp = House(n,1,16,cross,[],[],[],[])
    assert sorted(opp.elevations()) == sorted(["CR","PR","CL"])

##Only two of the across houses have set elevations
def test_Elevation3Across2Set():
    cross = [(n,5,17),(n,5,18),(n,5,19)]
    opp = House(n,5,20,cross,[],[],[],[])
    assert opp.elevations() == ["CR","PR"]

##4 Houses Across "CL" and "CR" Elevations
def test_Elevation4Across():
    cross = [(n,6,21),(n,6,22),(n,6,23),(n,6,24)]
    opp = House(n,6,25,cross,[],[],[],[])
    assert opp.elevations() == ["PR"]

##5 Houses Across all elevations used, empty expected
def test_Elevation4Across():
    cross = [(n,7,26),(n,7,27),(n,7,28),(n,7,29),(n,7,30)]
    opp = House(n,7,31,cross,[],[],[],[])
    assert opp.elevations() == []

##Tests the case where a model elevation is under 30% of the block, importatnt that CL is in the list for this test
def test_Elevation30PercentRuleUnder():
    opp = House(n,20,1,[],[],[],[],[])
    assert sorted(opp.elevations()) == sorted(["CR","PR","CL"])

##Tests the case where a model elevation is equal to 30% of the block, important that PR is in the list for this test.
def test_Elevation30PercentRuleEqual():
    opp = House(n,30,1,[],[],[],[],[])
    assert sorted(opp.elevations()) == sorted(["CR","PR","CL"])

##Tests teh case where a model elevation is over 30% of the block.
def test_Elevation30PercentRuleOver():
    opp = House(n,40,1,[],[],[],[],[])
    assert sorted(opp.elevations()) == sorted(["CR","CL"])

##Tests the case for 3 in row, with this house being the middle one
def test_Elevation3InRow1EachSize():
    left = [None,(n,100,2)]
    right = [(n,100,4),None]
    opp = House(n,100,1,[],left,right,[],[])
    assert opp.elevations() == ["CR"]

##Tests the case for 3 in row, with this house being the leftmost one
def test_Elevation3InRow2Right():
    right = [(n,100,2),(n,100,3)]
    opp = House(n,100,1,[],[],right,[],[])
    assert opp.elevations() == ["PR"]

##Tests the case for 3 in row, with this house being the rightmost one
def test_Elevation3InRow2Left():
    left = [(n,100,2),(n,100,3)]
    opp = House(n,100,1,[],left,[],[],[])
    assert opp.elevations() == ["PR"]

def test_Elevation2AppartOneAwayLeft():
    left = [None,(n,100,2)]
    opp = House(n,100,1,[],left,[],[],[])
    assert sorted(opp.elevations()) == sorted(["CR","PR"])

def test_Elevation2AppartTwoAwayLeft():
    left = [(n,100,3),None]
    opp = House(n,100,1,[],left,[],[],[])
    assert sorted(opp.elevations()) == sorted(["CL","PR"])

def test_Elevation2AppartOneAwayRight():
    right = [(n,100,3),None]
    opp = House(n,100,1,[],[],right,[],[])
    assert sorted(opp.elevations()) == sorted(["CL","PR"])

def test_Elevation2AppartTwoAwayRight():
    right = [None,(n,100,4)]
    opp = House(n,100,1,[],[],right,[],[])
    assert sorted(opp.elevations()) == sorted(["CL","CR"])

def test_ElevationConers1Corner():
    corn = [(n,100,4)]
    opp = House(n,100,1,[],[],[],corn,[])
    assert sorted(opp.elevations()) == sorted(["CL","CR"])

def test_ElevationConers3Corners():
    corn = [(n,100,4),(n,100,3),(n,100,2)]
    opp = House(n,100,1,[],[],[],corn,[])
    assert opp.elevations() == []

