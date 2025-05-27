import numpy as np
from Utilities.DirectionHelper import DirectionHelper

def test_rotate_right_90_succesful():
    expected = np.array([0, -1])
    vec = np.array([1,0]) # from EAST to SOUTH
    
    result = DirectionHelper.rotate_right_90(vec)
    assert np.array_equal(result, expected) is True
    
def test_rotate_left_90_succesful():
    vec = np.array([0, 1]) # from NORTH to WEST
    expected = np.array([-1, 0])
    
    result = DirectionHelper.rotate_left_90(vec)
    assert np.array_equal(result, expected) is True