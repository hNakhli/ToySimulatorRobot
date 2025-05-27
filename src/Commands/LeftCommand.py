from Commands.AbstractCommand import AbstractCommand
from RobotProvider import RobotProvider
from Utilities.Log import Log
from Utilities.DirectionHelper import DirectionHelper

class LeftCommand(AbstractCommand):
    logger:Log = None
    
    def __init__(self, logger:Log, robotProvider:RobotProvider):
        self.logger = logger
        self.robotProvider = robotProvider
    
    def TryParse(self, line:str) -> bool:
        if line.startswith("LEFT"):
            return True
        return False
    
    def TryExecute(self) -> bool:
        self.logger.Debug("trying to execute LEFT commmand: " + type(self).__name__)
        
        robot = self.robotProvider.get_robot()
        # Validate
        if robot is None:
            self.logger.Error("No robot could be found")
            return False
        
        # Execute
        self.logger.Debug("before: " + robot.Direction)
        robot.Direction = DirectionHelper.rotate_left_90(robot.Direction)
        self.logger.Debug("after: " + robot.Direction)
        self.logger.Debug("Command succesful" + type(self).__name__)
        return True
        
    