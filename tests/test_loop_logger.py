import pytest
import logging
import io
import sys
from src.loop_logger import log_variables_in_loop

def test_log_variables_in_loop_default():
    # Capture logging output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    # Test with a list
    test_list = [1, 2, 3]
    result = log_variables_in_loop(test_list)
    
    # Check the result
    assert result == test_list
    
    # Check log output
    log_output = log_capture.getvalue()
    assert "Loop iteration 0: Value = 1" in log_output
    assert "Loop iteration 1: Value = 2" in log_output
    assert "Loop iteration 2: Value = 3" in log_output

def test_log_variables_in_loop_different_levels():
    # Test different log levels
    log_levels = [
        logging.DEBUG, 
        logging.INFO, 
        logging.WARNING, 
        logging.ERROR, 
        logging.CRITICAL
    ]
    
    for level in log_levels:
        # Capture logging output
        log_capture = io.StringIO()
        logging.basicConfig(stream=log_capture, level=level)
        
        test_list = [10, 20]
        result = log_variables_in_loop(test_list, log_level=level)
        
        assert result == test_list

def test_log_variables_in_loop_empty_iterable():
    # Test with an empty iterable
    result = log_variables_in_loop([])
    assert result == []

def test_log_variables_in_loop_different_types():
    # Test with different types of iterables
    test_cases = [
        [1, 2, 3],
        ('a', 'b', 'c'),
        {'x': 1, 'y': 2},
        {1, 2, 3}
    ]
    
    for test_case in test_cases:
        result = log_variables_in_loop(test_case)
        assert list(result) == list(test_case)