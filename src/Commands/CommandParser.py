from Commands import AbstractCommand
from Utilities.Log import Log

class CommandParser:
    abstractCommands: list[AbstractCommand.AbstractCommand] = []
    logger:Log
    
    def __init__(self, logger:Log):
        self.abstractCommands = []
        self.logger = logger
        
    def Register(self, command: AbstractCommand.AbstractCommand):
        self.logger.Debug("registering command: " + command.name)
        self.abstractCommands.append(command)
        
    def TryExecute(self, line: str) -> bool:
        self.logger.Debug("Attempting to find a match for: " + line)
        for command in self.abstractCommands:
            if command.TryParse(line) is True:
                command.TryExecute()
                return True
        self.logger.Info("No matching command was found for: " + line)
        return False
            
        