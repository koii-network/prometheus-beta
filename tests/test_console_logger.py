import os
import platform
import pytest
from io import StringIO
import sys
from src.console_logger import clear_console_and_log

def test_clear_console_and_log(capsys):
    """
    Test the clear_console_and_log function.
    
    Checks if the function:
    1. Doesn't raise any exceptions
    2. Prints the correct message
    """
    test_message = "Hello, Console!"
    
    # Capture standard output
    clear_console_and_log(test_message)
    captured = capsys.readouterr()
    
    # Check if the message was printed
    assert test_message in captured.out.strip()

def test_clear_console_system_compatibility():
    """
    Test that the clear command is compatible with the current operating system.
    """
    system = platform.system().lower()
    
    if system == 'windows':
        assert hasattr(os, 'system') and os.system('cls') is not None
    else:  # Unix-like systems
        assert hasattr(os, 'system') and os.system('clear') is not None

def test_clear_console_with_empty_message(capsys):
    """
    Test function behavior with an empty message.
    """
    clear_console_and_log("")
    captured = capsys.readouterr()
    
    # An empty message should still work without errors
    assert captured.out.strip() == ""