For this exercise, we would need to extract the commands from a text file. Each command would need to have an abstract parsing method and an abstract action. This way we would be able to extend it easily. A good starting point can be defining this abstract methods for parsing the text file. Currently the expected design would look something similar to the following diagram:
![Updated Diagram](/Docs/Images/Updated%20Diagram.png)

The implementation can be broken into the following tasks
[TASK-3 Implement a logger](TASK-3%20Implement%20a%20logger.md)
[TASK-4 Defining a generic parsing method and logging the results into the console](TASK-4%20Defining%20a%20generic%20parsing%20method%20and%20logging%20the%20results%20into%20the%20console.md)
[TASK-5 implementing commands and validation](TASK-5%20implementing%20commands%20and%20validation.md)

Note: the name of Map was changed to Region as it was ambiguous (with the internal map function in python)
## Coordinate system
Normal Cartesian coordinate system has been used for this project as the robot is not performing any complex movements and the map is defined as a grid (rectangle/square).
![Cartesian Coordinate System](/Docs/Images/Cartesian%20Coordinate%20System.png)
With respect to rotation and angles, the following convention is used:
![Angles and units](/Docs/Images/Angles%20and%20units.png)

## Helpers
There are two helper classes added: 
1. **Logging utility**: this is to ensure we can easily turn of logging from everywhere (and/or change the underlying output format)
2. **Direction Helper:** This class was added to help with the angles and rotations
## Commands
Commands would be the way we would interact with the robots and the map. Commands would provide few main functionality:
1. Allowing an abstract parsing method / method definition to extract the required parameters from the text file.
2. Performing validation to ensure incorrect requests are not performed
3. Allowing an abstract action to be performed depending on the robot.
#### PLACE
This command creates and places a robot in the map. This command must be called first for each robot before they are allowed to perform any other commands.

**Validations:**
- Validation required for x, y position - it must be within the boundary of the map
- The face parameter must be one of the following: NORTH, SOUTH, EAST, WEST
**Assumptions:** 
- x, y at the moment are assumed to be doubles - but the logic could be changed to validate them to ensure they are only integers
- At the moment, it is assumed that there are no obstructions 
### MOVE
Move would be moving the robot forward one unit in the forward direction.

**Validation:** 
- Ignore if the robot is not placed first
- Robot cannot move outside of the boundary of the map
### Rotations (LEFT / RIGHT)
Robot direction can be rotated by 90 degrees in LEFT or RIGHT direction

**Validation:** 
- Ignore if the robot is not placed first

**Assumptions:**
- In Designing the robot, it is assumed that this functionality could / might be extended in future to have custom angles
### REPORT
This command would report the position of the robot - at the moment it would follow this format: x,y,FACE.

**Validation:** 
- Ignore if the robot is not placed first