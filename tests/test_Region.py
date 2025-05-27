from Region import Region

def test_region_inbound_succesfull():
    region = Region(0, 0, 5, 5)
    assert region.in_bound(0, 0) is True
    assert region.in_bound(1.5, 0) is True

def test_region_inbound_unsuccesfull():
    region = Region(0, 0, 5, 5)
    assert region.in_bound(10, 10) is False
    assert region.in_bound(-1, 0) is False