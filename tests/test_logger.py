import io
import sys
import pytest
from src.logger import log_message

def test_log_message(capsys):
    """
    Test that log_message prints the correct message to console.
    """
    test_message = "Hello, logging!"
    log_message(test_message)
    
    # Capture the printed output
    captured = capsys.readouterr()
    assert captured.out.strip() == test_message

def test_log_message_different_types():
    """
    Test logging different types of messages.
    """
    # Test with integer
    log_message(42)
    # Test with float
    log_message(3.14)
    # Test with boolean
    log_message(True)

def test_log_message_empty_string(capsys):
    """
    Test logging an empty string.
    """
    log_message("")
    captured = capsys.readouterr()
    assert captured.out.strip() == ""