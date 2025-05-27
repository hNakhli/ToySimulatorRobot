import pytest
from Commands.PlaceCommand import PlaceCommand
from Face import Face

from Utilities.test_Log_provider import TestLogProvider

@pytest.fixture
def UnderTest():
    log = TestLogProvider()
    return PlaceCommand(log)

def test_correct_parsing_pass(UnderTest):
    assert UnderTest.TryParse("PLACE 4,5,NORTH") is True
    assert UnderTest.x == 4
    assert UnderTest.y == 5
    assert UnderTest.face == Face.NORTH

def test_decimal_coordinate_parsing_fails(UnderTest):
    assert UnderTest.TryParse("PLACE 4.4,5.5,WEST") is False
    
def test_incorrect_Face_parsing_fails(UnderTest):
    assert UnderTest.TryParse("PLACE 4.4,5.5,INCORRECT") is False
