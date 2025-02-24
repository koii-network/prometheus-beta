import pytest
import logging
import io
import sys
from src.variable_type_logger import log_variable_type

def test_log_variable_type():
    # Capture logging output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO, 
                        format='%(asctime)s - Variable Type Logger - %(levelname)s: %(message)s')
    
    # Test different types of variables
    test_cases = [
        (42, 'int'),
        ('hello', 'str'),
        (3.14, 'float'),
        ([1, 2, 3], 'list'),
        ({'a': 1}, 'dict'),
        ((1, 2), 'tuple'),
        (True, 'bool'),
        (None, 'NoneType')
    ]
    
    for variable, expected_type in test_cases:
        # Call the function and check return value
        result = log_variable_type(variable)
        assert result == expected_type
        
        # Check logging output
        log_output = log_capture.getvalue()
        assert f"Variable type: {expected_type}" in log_output
        
        # Clear the log capture for next iteration
        log_capture.truncate(0)
        log_capture.seek(0)