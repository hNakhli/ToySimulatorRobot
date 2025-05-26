The main aim of this task is to have a generic parsing functionality and add the example files into the package so lines can be parsed.

----
## Acceptance Criteria
- **AC 1:** if a line did not have a matching command, an error should be logged into the console
- **AC 2:** if a line had a pattern matched, a debug level log should be added to the log file
## Design Constraints
Both actions and parsing methods should be abstract so this functionality remain easily extendable for adding future commands.