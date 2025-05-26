import numpy as np
from Robot import Robot

def main():
    print("Hello from toyrobotsimulator!")

if __name__ == "__main__":
    main()
    robot = Robot("Robot1", np.array((1,2)), np.array((0,1)), "NORTH")
    str = robot.Report()
    print(str)