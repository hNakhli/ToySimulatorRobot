from Commands.AbstractCommand import AbstractCommand
from Region import Region
from RobotProvider import RobotProvider
from Utilities.Log import Log

class MoveCommand(AbstractCommand):
    logger:Log = None
    
    def __init__(self, logger:Log, robotProvider:RobotProvider, region:Region):
        self.logger = logger
        self.robotProvider = robotProvider
        self.region = region
    
    def TryParse(self, line:str) -> bool:
        if line.startswith("MOVE"):
            return True
        return False
    
    def TryExecute(self) -> bool:
        self.logger.Debug("trying to execute MOVE commmand: " + type(self).__name__)
        
        robot = self.robotProvider.get_robot()
        # Validate
        if robot is None:
            self.logger.Error("No robot could be found")
            return False
        
        # Checking that the next position should be within map boundary
        nextLocation = robot.Position + robot.Direction
        checkPos = self.region.in_bound(nextLocation[0], nextLocation[1])
        if checkPos is False:
            self.logger.Error("Move Prevented: The next location will not be within the movement region")
            return False
        
        # Execute
        self.logger.Debug("before: " + str(robot.Position))
        robot.Position = nextLocation
        self.logger.Debug("after: " + str(robot.Position))
        return True
        
    