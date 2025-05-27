import pytest
from Commands.PlaceCommand import PlaceCommand
from Face import Face

from Region import Region
from RobotProvider import RobotProvider
from Utilities.test_Log_provider import TestLogProvider

@pytest.fixture
def UnderTest():
    log = TestLogProvider()
    robotProvider = RobotProvider()
    region = Region(0, 0, 5, 5)
    return PlaceCommand(log, robotProvider, region)

def test_correct_parsing_pass(UnderTest):
    assert UnderTest.TryParse("PLACE 4,5,NORTH") is True
    assert UnderTest.x == 4
    assert UnderTest.y == 5
    assert UnderTest.face == Face.NORTH

def test_decimal_coordinate_parsing_fails(UnderTest):
    assert UnderTest.TryParse("PLACE 4.4,5.5,WEST") is False
    
def test_incorrect_Face_parsing_fails(UnderTest):
    assert UnderTest.TryParse("PLACE 4.4,5.5,INCORRECT") is False
    
def test_incorrect_location_would_not_execute(UnderTest):
    UnderTest.TryParse("PLACE 10,10,NORTH")
    assert UnderTest.TryExecute() is False
