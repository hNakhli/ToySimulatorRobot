import pytest
from Commands.CommandParser import CommandParser
from Commands.LeftCommand import LeftCommand
from Commands.MoveCommand import MoveCommand
from Commands.PlaceCommand import PlaceCommand
from Commands.ReportCommand import ReportCommand
from Commands.RightCommand import RightCommand
from Face import Face
from Region import Region
from RobotProvider import RobotProvider
from Utilities.Log import Log
from main import ParseFromFile
import os

# This is mostly the integration tests at the file input level
# There are potentially better ways of separating the txt parsing/provider
# class to enable mocking of the functionality.
@pytest.fixture
def setup():
    logger = Log()
    logger.enabled = False
    
    parser = CommandParser(logger)
    robotProvider = RobotProvider()
    region = Region(0, 0, 5, 5)
    
    parser.Register(LeftCommand(logger, robotProvider))
    parser.Register(RightCommand(logger, robotProvider))
    parser.Register(MoveCommand(logger, robotProvider, region))
    parser.Register(PlaceCommand(logger, robotProvider, region))
    parser.Register(ReportCommand(logger, robotProvider))
    return (parser, robotProvider)

def test_example_1(setup):
    currentPath = os.path.dirname(__file__)
    file = "Example3.txt"
    absPath = os.path.join(currentPath, file)

    (parser, robotProvider) = setup
    ParseFromFile(absPath, parser)
    robot = robotProvider.get_robot()
    
    assert robot.Report() == "3,3,NORTH"
    
# Potentially an improvement on this could be to
# parametrize it using pytest so an input file name, 
# and an expected report at the end are used for verification
def test_trying_all_commands(setup):
    currentPath = os.path.dirname(__file__)
    file = "TryingAllCommands.txt"
    absPath = os.path.join(currentPath, file)

    (parser, robotProvider) = setup
    ParseFromFile(absPath, parser)
    robot = robotProvider.get_robot()
    
    assert robot.Report() == "0,5,NORTH"