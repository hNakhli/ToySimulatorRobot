import pytest
import numpy as np
from Commands.MoveCommand import MoveCommand
from Face import Face

from Region import Region
from RobotProvider import RobotProvider
from Utilities.test_Log_provider import TestLogProvider

def test_tryexecute_should_not_exceed_region():
    log = TestLogProvider()
    robotProvider = RobotProvider()
    robotProvider.place_robot(5, 5, Face.NORTH)
    region = Region(0, 0, 5, 5)
    cmnd = MoveCommand(log, robotProvider, region)
    
    assert cmnd.TryExecute() is False
    
def test_tryexecute_should_move_correctly():
    # Setup 
    log = TestLogProvider()
    robotProvider = RobotProvider()
    robotProvider.place_robot(0, 0, Face.NORTH)
    region = Region(0, 0, 5, 5)
    cmnd = MoveCommand(log, robotProvider, region)
    expected = np.array([0, 1])
    
    # Action
    cmnd.TryExecute()
    robot = robotProvider.get_robot()
    
    # Assert
    assert np.array_equal(robot.Position, expected) is True
    