from Commands.AbstractCommand import AbstractCommand
from Utilities.Log import Log

class LeftCommand(AbstractCommand):
    logger:Log = None
    
    def __init__(self, logger:Log):
        self.logger = logger
    
    def TryParse(self, line:str) -> bool:
        if line.startswith("LEFT"):
            return True
        return False
    
    def TryExecute(self) -> bool:
        self.logger.Debug("tried to execute LEFT commmand: " + type(self).__name__)
        return True
        
    