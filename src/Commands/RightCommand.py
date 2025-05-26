from Commands.AbstractCommand import AbstractCommand
from Utilities.Log import Log

class RightCommand(AbstractCommand):
    logger:Log = None
    
    def __init__(self, logger:Log):
        self.logger = logger
    
    def TryParse(self, line:str) -> bool:
        if line.startswith("RIGHT"):
            return True
        return False
    
    def TryExecute(self) -> bool:
        self.logger.debug("tried to execute RIGHT commmand: " + type(self).__name__)
        return True
        
    