from Commands.AbstractCommand import AbstractCommand
from RobotProvider import RobotProvider
from Utilities.Log import Log

class ReportCommand(AbstractCommand):
    logger:Log = None
    
    def __init__(self, logger:Log, robotProvider:RobotProvider):
        self.logger = logger
        self.robotProvider = robotProvider
    
    def TryParse(self, line:str) -> bool:
        if line.startswith("REPORT"):
            return True
        return False
    
    def TryExecute(self) -> bool:
        self.logger.Debug("trying to execute REPORT commmand: " + type(self).__name__)
        
        robot = self.robotProvider.get_robot()
        # Validate
        if robot is None:
            self.logger.Error("No robot could be found")
            return False
        
        # Execute
        value = robot.Report()
        
        # this is an assumption that the output is console - in reality
        # this should be inejcted into the class so we could replace /
        # test it
        print(value) 
        
        return True
        
    