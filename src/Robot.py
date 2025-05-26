import numpy as np

class Robot:
    Position:np.array = ((0,0))
    Direction:np.array = ((1,0))
    Identity:str = None
    Face = None
    
    def __init__(self, identity:str, Position:np.array, Direction:np.array, face:str):
        self.Position = Position
        self.Direction = Direction
        self.Identity = identity
        self.Face = face
        
    def Report(self) -> str:
        return str(int(self.Position[0])) + "," + str(int(self.Position[1])) + "," + self.Face