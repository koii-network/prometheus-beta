import io
import sys
import pytest
from src.logger import log_message

def test_log_message_prints_correctly(capsys):
    """
    Test that log_message prints the provided message to the console.
    """
    test_message = "Hello, logging!"
    log_message(test_message)
    
    # Capture the printed output
    captured = capsys.readouterr()
    
    # Assert that the printed output matches the input message
    assert captured.out.strip() == test_message

def test_log_message_with_empty_string(capsys):
    """
    Test logging an empty string.
    """
    log_message("")
    captured = capsys.readouterr()
    assert captured.out.strip() == ""

def test_log_message_with_different_types():
    """
    Test logging different types of messages, 
    ensuring the function can handle various input types.
    """
    # Test with integer
    with pytest.raises(TypeError):
        log_message(42)
    
    # Test with None
    with pytest.raises(TypeError):
        log_message(None)