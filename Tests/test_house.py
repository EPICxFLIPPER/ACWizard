##Note To LIAM, you can run tests just by typing pytest when in the Tests directory

import pytest

def test_simple():
    assert 1 + 1 == 2

@pytest.mark.skip(reason="This test is not done")
def test_Elevation3Across():
    print("stub")

@pytest.mark.skip(reason="This test is not done")
def test_Elevation7Across():
    print("stub")

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