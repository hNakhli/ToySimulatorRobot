The main aim of this Task is to implement the remaining commands validations and executions

---
## Acceptance Criteria
- **AC 1:** The robot must be placed within the boundary of the map
- **AC 2:** The robot must not fall out of the map
- **AC 3:** Any invalid commands would be skipped and a console log message would be provided to notify the user of the issue (This could be moved into a log file instead)
## Design constraints
- It would be best to keep the rotations as generics and use the directions to move the robot to LEFT and RIGHT - this would require an adapter to translate from Direction into the keywords provided in the requirements (SOUTH, EAST, NORTH, WEST)