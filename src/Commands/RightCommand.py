from Commands.AbstractCommand import AbstractCommand
import RobotProvider
from Utilities.Log import Log
from Utilities.DirectionHelper import DirectionHelper

class RightCommand(AbstractCommand):
    logger:Log = None
    
    def __init__(self, logger:Log, robotProvider:RobotProvider):
        self.logger = logger
        self.robotProvider = robotProvider
    
    def TryParse(self, line:str) -> bool:
        if line.startswith("RIGHT"):
            return True
        return False
    
    def TryExecute(self) -> bool:
        self.logger.Debug("tried to execute RIGHT commmand: " + type(self).__name__)
        
        robot = self.robotProvider.get_robot()
        # Validate
        if robot is None:
            self.logger.Error("No robot could be found")
            return False
        
        # Execute
        self.logger.Debug("before: " + str(robot.Direction))
        robot.Direction = DirectionHelper.rotate_right_90(robot.Direction)
        self.logger.Debug("after: " + str(robot.Direction))
        self.logger.Debug("Command succesful" + type(self).__name__)
        return True
        
    