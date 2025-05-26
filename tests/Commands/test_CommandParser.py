import pytest
from Commands.CommandParser import CommandParser
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
    testInputLine = "MOVE"
    assert UnderTest.TryExecute(testInputLine) is True
        
def test_register_adds_command(UnderTest):
    underTest = UnderTest
    #underTest.Register()
    assert len(underTest.abstractCommands) > 0
