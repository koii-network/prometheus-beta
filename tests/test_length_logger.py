import pytest
import logging
from src.length_logger import log_length

def test_log_length_string():
    """Test logging length of a string"""
    # Capture logs
    with pytest.raises(TypeError):
        log_length(123)  # Non-string/list/tuple should raise TypeError

def test_log_length_valid_inputs(caplog):
    """Test logging length of various valid inputs"""
    # Test string
    caplog.set_level(logging.INFO)
    assert log_length("hello") == 5
    assert "Length of item: 5" in caplog.text

    # Reset caplog
    caplog.clear()

    # Test list
    assert log_length([1, 2, 3]) == 3
    assert "Length of item: 3" in caplog.text

    # Reset caplog
    caplog.clear()

    # Test tuple
    assert log_length(('a', 'b', 'c', 'd')) == 4
    assert "Length of item: 4" in caplog.text

def test_log_length_empty_inputs(caplog):
    """Test logging length of empty inputs"""
    caplog.set_level(logging.INFO)
    
    # Empty string
    assert log_length("") == 0
    assert "Length of item: 0" in caplog.text

    # Reset caplog
    caplog.clear()

    # Empty list
    assert log_length([]) == 0
    assert "Length of item: 0" in caplog.text

def test_log_length_error_handling():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be a string, list, or tuple"):
        log_length({"key": "value"})  # Dictionary should raise TypeError
    
    with pytest.raises(TypeError, match="Input must be a string, list, or tuple"):
        log_length(42)  # Integer should raise TypeError
    
    with pytest.raises(TypeError, match="Input must be a string, list, or tuple"):
        log_length(3.14)  # Float should raise TypeError