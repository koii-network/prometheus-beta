import io
import sys
import pytest
from src.console_logger import log_message

def test_log_message(capsys):
    """
    Test that log_message prints the given message to console.
    
    Args:
        capsys: Pytest fixture to capture print output
    """
    test_message = "Hello, logging!"
    log_message(test_message)
    
    # Capture the printed output
    captured = capsys.readouterr()
    
    # Assert the message was printed correctly
    assert captured.out.strip() == test_message

def test_log_message_empty_string(capsys):
    """
    Test logging an empty string.
    
    Args:
        capsys: Pytest fixture to capture print output
    """
    log_message("")
    
    # Capture the printed output
    captured = capsys.readouterr()
    
    # Assert an empty string can be logged
    assert captured.out.strip() == ""

def test_log_message_different_types():
    """
    Test logging different types of messages.
    """
    # Test integer
    log_message(42)
    
    # Test float
    log_message(3.14)
    
    # Test list
    log_message([1, 2, 3])
    
    # Test dictionary
    log_message({"key": "value"})