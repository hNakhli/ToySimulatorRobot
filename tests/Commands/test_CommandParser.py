import pytest
from Commands.LeftCommand import LeftCommand
from Commands.CommandParser import CommandParser
from Commands.RightCommand import RightCommand
from Utilities.test_Log_provider import TestLogProvider

@pytest.fixture
def UnderTest():
    log = TestLogProvider()
    return CommandParser(log)

def test_parse_command_not_found(UnderTest):
    testInputLine = "MOVE"
    assert UnderTest.TryExecute(testInputLine) is False

def test_init_has_empty_command(UnderTest):
    assert len(UnderTest.abstractCommands) == 0
    
## Integration Test with a test command:
def test_parse_command_found(UnderTest):
    testInputLine = "LEFT"
    leftCommand = LeftCommand(TestLogProvider())
    UnderTest.Register(leftCommand)
    assert UnderTest.TryExecute(testInputLine) is True
    
def test_parse_multiple_commands_found(UnderTest):
    testInputLine = "LEFT"
    leftCommand = LeftCommand(TestLogProvider())
    rightCommand = RightCommand(TestLogProvider())
    UnderTest.Register(leftCommand)
    UnderTest.Register(rightCommand)
    
    assert UnderTest.TryExecute(testInputLine) is True
    assert len(UnderTest.abstractCommands) > 1

def test_register_adds_command(UnderTest):
    leftCommand = LeftCommand(TestLogProvider())
    UnderTest.Register(leftCommand)
    assert len(UnderTest.abstractCommands) > 0
