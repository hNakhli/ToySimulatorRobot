import numpy as np
   
class DirectionHelper:
    @staticmethod
    def rotate_right_90(direction : np.array) -> np.array:
        # Clockwise rotation matrix (RIGHT)
        return np.array([[0, -1], [1, 0]]) @ direction
    
    @staticmethod
    def rotate_left_90(direction : np.array) -> np.array:
        # Counter clockwise rotation matrix (LEFT)
        return np.array([[0, 1], [-1, 0]]) @ direction
    