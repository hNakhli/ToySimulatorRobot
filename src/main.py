import numpy as np
from Robot import Robot
from Utilities.log import Log

if __name__ == "__main__":
    logger = Log()
    logger.Info("TEST 1")
    logger.Debug("TEST 2")
    logger.Info("TEST 3")
    
    robot = Robot("Robot1", np.array((1,2)), np.array((0,1)), "NORTH")
    str = robot.Report()
    print(str)