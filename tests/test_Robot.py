from Robot import Robot
import numpy as np

def test_Report_pass():
    underTest = createRobot()
    value = underTest.Report()
    assert value == "1,2,NORTH"

def test_Report_decimalpoint_notprinted():
    underTest = createRobot()
    underTest.Position = np.array((1.5, 2.5))
    value = underTest.Report()
    assert value == "1,2,NORTH"
    
def createRobot() -> Robot:
    return Robot("Robot1", np.array((1.5,2.3)), np.array((1,1)), "NORTH")