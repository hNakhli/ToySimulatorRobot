from Commands.CommandParser import CommandParser

from Commands.LeftCommand import LeftCommand
from Commands.MoveCommand import MoveCommand
from Commands.PlaceCommand import PlaceCommand
from Commands.RightCommand import RightCommand
from Commands.ReportCommand import ReportCommand
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
    parser = CommandParser(logger)
    
    parser.Register(LeftCommand(logger))
    parser.Register(RightCommand(logger))
    parser.Register(MoveCommand(logger))
    parser.Register(PlaceCommand(logger))
    parser.Register(ReportCommand(logger))
    
    currentPath = os.path.dirname(__file__)
    subFolder = "Examples"
    file = "Example3.txt"
    absPath = os.path.join(currentPath, subFolder, file)
    
    ParseFromFile(absPath, parser)
        
