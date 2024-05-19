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

##All 3 houses across have CL elevation
def test_Elevation3AcrossSame():
    cross = [(n,1,5),(n,1,6),(n,1,7)]
    opp = House(n,1,8,cross,[],[],[],[])
    assert sorted(opp.elevations()) == sorted(["CR","PR"])

##All 3 houses across have different elevation, expect empty return
def test_Elevation3AcrossAll():
    cross = [(n,1,9),(n,1,10),(n,1,11)]
    opp = House(n,1,12,cross,[],[],[],[])
    assert opp.elevations() == []

##All 3 houses across have no set elevation
def test_Elevation3AcrossEmpty():
    cross = [(n,1,13),(n,1,14),(n,1,15)]
    opp = House(n,1,16,cross,[],[],[],[])
    assert sorted(opp.elevations()) == sorted(["CR","PR","CL"])

##Only two of the across houses have set elevations
def test_Elevation3Across2Set():
    cross = [(n,1,17),(n,1,18),(n,1,19)]
    opp = House(n,1,20,cross,[],[],[],[])
    assert opp.elevations() == ["PR"]

##4 Houses Across "CL" and "CR" Elevations
def test_Elevation4Across():
    cross = [(n,1,21),(n,1,22),(n,1,23),(n,1,24)]
    opp = House(n,1,25,cross,[],[],[],[])
    assert opp.elevations() == ["PR"]

##5 Houses Across all elevations used, empty expected
def test_Elevation4Across():
    cross = [(n,1,26),(n,1,27),(n,1,28),(n,1,29),(n,1,30)]
    opp = House(n,1,31,cross,[],[],[],[])
    assert opp.elevations() == []


@pytest.mark.skip(reason="This test is not done")
def test_Elevation30PercentRule():
    print("stub")

@pytest.mark.skip(reason="This test is not done")
def test_Elevation3InRow():
    print("stub")

@pytest.mark.skip(reason="This test is not done")
def test_Elevation2Appart():
    print("stub")

@pytest.mark.skip(reason="This test is not done")
def test_ElevationConers():
    print("stub")

@pytest.mark.skip(reason="This test is not done")
def test_elevationGeneral():
    print("stub")