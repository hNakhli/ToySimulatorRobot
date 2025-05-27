from Commands.AbstractCommand import AbstractCommand
from Region import Region
from RobotProvider import RobotProvider
from Utilities.Log import Log
from Face import Face

class PlaceCommand(AbstractCommand):
    logger:Log = None
    face:str = None
    x:int = None
    y:int = None
    
    def __init__(self, logger:Log, robotProvider:RobotProvider, region:Region):
        self.logger = logger
        self.robotProvider = robotProvider
        self.region = region
        
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
                face = face.upper()
                
                if Face.face_exists(face):
                    self.logger.Debug("Requested face " + face + " is not valid")
                    return False
                
                self.face = Face[face]
                                
                return True
            except Exception as e:
                self.logger.Debug("Failed to parse: " + format(e))
        return False
    
    def TryExecute(self) -> bool:
        self.logger.Debug("trying to execute PLACE commmand: " + type(self).__name__)
        
        # Validate
        if self.region.in_bound(self.x, self.y) is False:
            self.logger.Error("The provided coordinates are out of bound")
            return False
        
        ## assuming this is already correct due to the parsing above
        self.robotProvider.place_robot(self.x, self.y, self.face)
        self.logger.Debug("Placed the robot in the requested coordinate")
        return True
        
    