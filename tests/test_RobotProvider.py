import pytest
from RobotProvider import RobotProvider
from Face import Face

@pytest.fixture
def GetProvider():
    return RobotProvider()

def test_get_robot_returns_none(GetProvider):
    robot = GetProvider.get_robot()
    assert robot is None
    
def test_place_robot_returns_succesfully(GetProvider):
    GetProvider.place_robot(1, 2, Face.NORTH)
    robot = GetProvider.get_robot()
    assert robot is not None    
    
def test_two_place_command_updates(GetProvider):
    GetProvider.place_robot(1, 2, Face.WEST)
    GetProvider.place_robot(3, 4, Face.NORTH)
    robot = GetProvider.get_robot()
    assert robot is not None
    assert len(GetProvider.robot_list) == 1