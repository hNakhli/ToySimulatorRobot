from abc import ABC, abstractmethod
from Utilities.Log import Log

class AbstractCommand(ABC):
    @abstractmethod
    def TryParse(self, line:str) -> bool:
        # attempt to parse a commmand - return true if succesful and false if not
        pass
    
    @abstractmethod
    def TryExecute(self) -> bool:
        # attempt to execute a commmand - return true if succesful and false if not
        pass