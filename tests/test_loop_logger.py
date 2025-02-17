import pytest
import logging
from src.loop_logger import log_loop_variables

def test_log_loop_variables_basic(caplog):
    """Test basic logging functionality"""
    caplog.set_level(logging.INFO)
    
    # Test with a list
    result = log_loop_variables([1, 2, 3])
    
    # Check return value
    assert result == [1, 2, 3]
    
    # Check log messages
    assert len(caplog.records) == 3
    assert "Loop iteration 0: value = 1" in caplog.text
    assert "Loop iteration 1: value = 2" in caplog.text
    assert "Loop iteration 2: value = 3" in caplog.text

def test_log_loop_variables_empty():
    """Test with an empty iterable"""
    result = log_loop_variables([])
    assert result == []

def test_log_loop_variables_custom_log_level(caplog):
    """Test with a custom log level"""
    caplog.set_level(logging.DEBUG)
    
    # Use DEBUG level
    result = log_loop_variables([4, 5, 6], log_level=logging.DEBUG)
    
    # Check return value
    assert result == [4, 5, 6]
    
    # Verify log messages at DEBUG level
    assert len(caplog.records) == 3
    for record in caplog.records:
        assert record.levelno == logging.DEBUG

def test_log_loop_variables_different_types():
    """Test with different types of iterables"""
    # Test with tuple
    result_tuple = log_loop_variables(('a', 'b', 'c'))
    assert result_tuple == ['a', 'b', 'c']
    
    # Test with set
    result_set = log_loop_variables({1, 2, 3})
    assert set(result_set) == {1, 2, 3}