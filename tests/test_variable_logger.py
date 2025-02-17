import pytest
import logging
import io
import sys
from src.variable_logger import log_variable_values

def test_log_variable_values_list():
    """Test logging a list of values."""
    # Capture log output
    log_capture = io.StringIO()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(log_capture)
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)
    
    # Test function
    result = log_variable_values([1, 2, 3], logger=logger)
    
    # Check results
    assert result == [1, 2, 3]
    log_output = log_capture.getvalue()
    assert "Iteration 0: Value = 1" in log_output
    assert "Iteration 1: Value = 2" in log_output
    assert "Iteration 2: Value = 3" in log_output

def test_log_variable_values_tuple():
    """Test logging a tuple of values."""
    # Capture log output
    log_capture = io.StringIO()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(log_capture)
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)
    
    # Test function
    result = log_variable_values(('a', 'b', 'c'), logger=logger)
    
    # Check results
    assert result == ['a', 'b', 'c']
    log_output = log_capture.getvalue()
    assert "Iteration 0: Value = a" in log_output
    assert "Iteration 1: Value = b" in log_output
    assert "Iteration 2: Value = c" in log_output

def test_log_variable_values_custom_log_level():
    """Test logging with a custom log level."""
    # Capture log output
    log_capture = io.StringIO()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(log_capture)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    # Test function
    result = log_variable_values([1, 2, 3], log_level=logging.DEBUG, logger=logger)
    
    # Check results
    assert result == [1, 2, 3]
    log_output = log_capture.getvalue()
    assert "Iteration 0: Value = 1" in log_output

def test_log_variable_values_empty_iterable():
    """Test logging an empty iterable."""
    # Capture log output
    log_capture = io.StringIO()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(log_capture)
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)
    
    # Test function
    result = log_variable_values([], logger=logger)
    
    # Check results
    assert result == []
    log_output = log_capture.getvalue()
    assert log_output.strip() == ""

def test_log_variable_values_non_iterable():
    """Test logging with a non-iterable input."""
    with pytest.raises(TypeError, match="Input must be an iterable"):
        log_variable_values(42)  # Integer is not iterable