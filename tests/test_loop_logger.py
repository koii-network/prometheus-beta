import pytest
import logging
from src.loop_logger import log_loop_variables

def test_log_loop_variables(caplog):
    # Test with a list of integers
    caplog.set_level(logging.INFO)
    result = log_loop_variables([10, 20, 30])
    
    assert result == [10, 20, 30]
    assert len(caplog.records) == 3
    assert "Loop iteration 0: value = 10" in caplog.text
    assert "Loop iteration 1: value = 20" in caplog.text
    assert "Loop iteration 2: value = 30" in caplog.text

def test_log_loop_variables_empty_list():
    # Test with an empty list
    result = log_loop_variables([])
    assert result == []

def test_log_loop_variables_mixed_types(caplog):
    # Test with mixed types
    caplog.set_level(logging.INFO)
    result = log_loop_variables(["apple", 42, True])
    
    assert result == ["apple", 42, True]
    assert len(caplog.records) == 3
    assert "Loop iteration 0: value = apple" in caplog.text
    assert "Loop iteration 1: value = 42" in caplog.text
    assert "Loop iteration 2: value = True" in caplog.text

def test_log_loop_variables_custom_log_level(caplog):
    # Test with a custom log level
    caplog.set_level(logging.DEBUG)
    result = log_loop_variables([1, 2, 3], log_level=logging.DEBUG)
    
    assert result == [1, 2, 3]
    assert len(caplog.records) == 3
    assert all(record.levelno == logging.DEBUG for record in caplog.records)