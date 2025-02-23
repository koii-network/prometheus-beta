import io
import sys
import pytest
from src.error_logger import log_error

def test_log_error_valid_message(capsys):
    """
    Test that a valid error message is correctly logged to stderr.
    """
    # Arrange
    test_message = "This is an error message"
    
    # Act
    log_error(test_message)
    
    # Assert
    captured = capsys.readouterr()
    assert captured.err.strip() == test_message

def test_log_error_empty_string(capsys):
    """
    Test logging an empty string.
    """
    # Act
    log_error("")
    
    # Assert
    captured = capsys.readouterr()
    assert captured.err.strip() == ""

def test_log_error_invalid_type():
    """
    Test that a TypeError is raised for non-string inputs.
    """
    # Arrange
    invalid_inputs = [
        42, 
        3.14, 
        None, 
        [], 
        {}, 
        True
    ]
    
    # Act & Assert
    for invalid_input in invalid_inputs:
        with pytest.raises(TypeError, match="Error message must be a string"):
            log_error(invalid_input)