import numpy as np
from enum import Enum

class Face(Enum):
    NORTH = (0, 1)
    EAST  = (1, 0)
    SOUTH = (0, -1)
    WEST  = (-1, 0)
    
    @staticmethod
    def from_vector(vector: np.array):
        try:
            for face in Face:
                val = face.value
                if vector[0] == val[0] and vector[1] == val[1]:
                    return face
        except Exception:
            # do nothing as it would return None
            return None
        return None
    
    @staticmethod 
    def get_matching_array(faceStr: str) -> np.array:
        for face in Face:
            if face.name == faceStr:
                return np.array([face.value[0], face.value[1]])
        return None
    
    @staticmethod
    def face_exists(faceStr: str) -> bool:
        return faceStr.upper in Face.__members__