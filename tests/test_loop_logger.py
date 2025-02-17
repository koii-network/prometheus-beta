import pytest
import logging
from src.loop_logger import log_loop_values

def test_log_loop_values_list():
    """Test logging with a list of integers"""
    test_list = [1, 2, 3, 4, 5]
    result = log_loop_values(test_list)
    assert result == test_list
    assert len(result) == 5

def test_log_loop_values_empty():
    """Test logging with an empty iterable"""
    result = log_loop_values([])
    assert result == []

def test_log_loop_values_strings():
    """Test logging with a list of strings"""
    test_strings = ['apple', 'banana', 'cherry']
    result = log_loop_values(test_strings)
    assert result == test_strings
    assert len(result) == 3

def test_log_loop_values_custom_log_level(caplog):
    """Test logging with a custom log level"""
    caplog.set_level(logging.WARNING)
    test_list = [10, 20, 30]
    result = log_loop_values(test_list, log_level=logging.WARNING)
    assert result == test_list
    
    # Check that log messages were created at WARNING level
    assert len(caplog.records) == 3
    for record in caplog.records:
        assert record.levelno == logging.WARNING