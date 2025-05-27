import pytest
from Map import Map

def test_map_inbound_succesfull():
    map = Map(0, 0, 5, 5)
    assert map.in_bound(0, 0) is True
    assert map.in_bound(1.5, 0) is True

def test_map_inbound_unsuccesfull():
    map = Map(0, 0, 5, 5)
    assert map.in_bound(10, 10) is False
    assert map.in_bound(-1, 0) is False