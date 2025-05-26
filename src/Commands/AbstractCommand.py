from abc import ABC, abstractmethod
from Utilities.Log import Log

class AbstractCommand(ABC):
    logger:Log = None
    parsed:bool = False
    
    def __init___(self, logger:Log):
        self.logger = logger
    
    @abstractmethod
    def TryParse(self, line:str) -> bool:
        # attempt to parse a commmand - return true if succesful and false if not
        pass
    
    def TryExecute(self) -> bool:
        # attempt to execute a commmand - return true if succesful and false if not
        self.logger.debug("I have executed the command  " + __class__.__name__)
    
    def PerformBaseValidation(self) -> bool:
        state = True
        if(self.parsed):
            self.logger.Info("Command " + __class__.__name__ + " not parsed correctly")
            state = False
        
        return state