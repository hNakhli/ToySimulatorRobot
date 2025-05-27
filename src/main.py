from Commands.CommandParser import CommandParser

from Commands.LeftCommand import LeftCommand
from Commands.MoveCommand import MoveCommand
from Commands.PlaceCommand import PlaceCommand
from Commands.RightCommand import RightCommand
from Commands.ReportCommand import ReportCommand
from Region import Region
from RobotProvider import RobotProvider
from Utilities.Log import Log
import os

def ParseFromFile(filepath: str, parser: CommandParser):
    with open(filepath, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            parser.TryExecute(line) 

if __name__ == "__main__":
    logger = Log()
    logger.enabled = True
    
    parser = CommandParser(logger)
    robotProvider = RobotProvider()
    region = Region(0, 0, 5, 5)
    
    parser.Register(LeftCommand(logger, robotProvider))
    parser.Register(RightCommand(logger, robotProvider))
    parser.Register(MoveCommand(logger, robotProvider, region))
    parser.Register(PlaceCommand(logger, robotProvider, region))
    parser.Register(ReportCommand(logger, robotProvider))
    
    currentPath = os.path.dirname(__file__)
    subFolder = "Examples"
    file = "ExampleFailingPath_MutliPlace.txt"
    absPath = os.path.join(currentPath, subFolder, file)
    
    ParseFromFile(absPath, parser)
        
