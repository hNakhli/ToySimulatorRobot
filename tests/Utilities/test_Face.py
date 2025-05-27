import numpy as np
from Face import Face

def test_from_vector():
    val = Face.NORTH.value
    face = Face.from_vector(np.array([val[0], val[1]]))
    
    assert face is Face.NORTH
    
def test_from_vector_returns_None():
    face = Face.from_vector(np.array([-2.5, 1.5]))
    assert face is None
    
def test_get_matching_coordinate_returns():
    expected = np.array([0, 1])
    array = Face.get_matching_array("NORTH")
    assert np.array_equal(array, expected) is True
    
def test_get_matching_coordinate_returns_None():
    array = Face.get_matching_array("TEST")
    assert array is None