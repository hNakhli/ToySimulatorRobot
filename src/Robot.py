import numpy as np
from Face import Face

# This is the base entity for the Robot
# Most logic / functionality has been kept away from this class
# and it is mostly treated as a plain object
class Robot:
    Position:np.array = ([0, 0])
    Direction:np.array = ([1, 0])
    Identity:str = None
    
    def __init__(self, identity:str, Position:np.array, face:Face):
        self.Position = Position
        self.Direction = np.array([face.value[0], face.value[1]])
        self.Identity = identity
        
    def Report(self) -> str:
        face = Face.from_vector(self.Direction)
        return str(int(self.Position[0])) + "," + str(int(self.Position[1])) + "," + face.name
    
    def UpdatePlacement(self, x, y, face: Face):
        self.Position = np.array((x, y))
        self.Direction = np.array([face.value[0], face.value[1]])
        self.Face = face