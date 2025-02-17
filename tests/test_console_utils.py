import os
import platform
import pytest
from src.console_utils import clear_console_and_log

def test_clear_console_and_log(capsys):
    """
    Test the clear_console_and_log function.
    
    This test verifies that:
    1. The function returns the message
    2. The message is printed
    3. No errors occur during console clearing
    """
    test_message = "Hello, Console Clearing Test!"
    
    # Call the function
    result = clear_console_and_log(test_message)
    
    # Check return value
    assert result == test_message
    
    # Capture the output
    captured = capsys.readouterr()
    assert test_message in captured.out

def test_clear_console_platform_compatibility():
    """
    Test that the clear console function doesn't raise exceptions on different platforms.
    """
    system = platform.system().lower()
    test_message = "Platform compatibility test"
    
    try:
        clear_console_and_log(test_message)
    except Exception as e:
        pytest.fail(f"clear_console_and_log raised an exception: {e}")

@pytest.mark.parametrize("message", [
    "Short message",
    "A longer message with multiple words",
    "",  # Empty string
    "Message with special characters: !@#$%^&*()"
])
def test_clear_console_log_variations(capsys, message):
    """
    Test clear_console_and_log with various message types.
    """
    result = clear_console_and_log(message)
    assert result == message
    
    captured = capsys.readouterr()
    assert message in captured.out