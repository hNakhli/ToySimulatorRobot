from Robot import Robot
import numpy as np
from Face import Face

class RobotProvider:
    
    '''
    Currently it is assumed that only one robot could be available on the surface
    '''
    identity = "ROBOT_1"
    robot_list: dict[str, Robot] = None
    
    '''
    It is assumed that this class is only created once in the application
    This could be changed to a static provider to ensure there is only a 
    singleton provider for robots.
    '''
    def __init__(self):
        self.robot_list = {}
        
    '''
    Gets and returns an instance of a robot. Bear in mind this can 
    return None and should be checked at the calling side
    '''
    def get_robot(self) -> Robot:
        return self.robot_list.get(self.identity)
    
    '''
    Initializes / places a robot on the map if a robot does not exist - it will 
    initialize it
    '''
    def place_robot(self, x:int, y:int, face:Face):
        if self.identity in self.robot_list:
            self.robot_list[self.identity].UpdatePlacement(x, y, face)
            return
        robot = Robot(self.identity, np.array([x, y]), face)
        self.robot_list[self.identity] = robot