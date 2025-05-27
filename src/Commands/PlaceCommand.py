from Commands.AbstractCommand import AbstractCommand
from Utilities.Log import Log
from Face import Face

class PlaceCommand(AbstractCommand):
    logger:Log = None
    face:str = None
    x:int = None
    y:int = None
    
    def __init__(self, logger:Log):
        self.logger = logger
        
    def ClearCache(self):
        self.face = None
        self.x = None
        self.y = None
    
    def TryParse(self, line:str) -> bool:
        self.ClearCache()
        if line.startswith("PLACE "):
            try:
                _, data = line.split("PLACE ", 1)
                x_str, y_str, face = map(str.strip, data.split(","))
                
                self.x = int(x_str)
                self.y = int(y_str)
                self.face = face.upper()
                
                if self.face not in Face.objects.all():
                    self.logger.Debug("Requested face " + self.face + " is not valid")
                    return False
                                
                return True
            except Exception as e:
                self.logger.Debug("Failed to parse: " + format(e))
        return False
    
    def TryExecute(self) -> bool:
        self.logger.Debug("tried to execute PLACE commmand: " + type(self).__name__)
        return True
        
    