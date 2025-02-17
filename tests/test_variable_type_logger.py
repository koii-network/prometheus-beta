import pytest
import logging
import io
import sys
from src.variable_type_logger import log_variable_type

def test_log_variable_type_basic_types():
    # Redirect logging to capture output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    # Test various basic types
    test_cases = [
        (42, 'int'),
        (3.14, 'float'),
        ('hello', 'str'),
        (True, 'bool'),
        ([1, 2, 3], 'list'),
        ((1, 2, 3), 'tuple'),
        ({1, 2, 3}, 'set'),
        ({'key': 'value'}, 'dict'),
        (None, 'NoneType')
    ]
    
    for variable, expected_type in test_cases:
        # Capture the return value and log output
        returned_type = log_variable_type(variable)
        
        # Check if the return value matches the expected type
        assert returned_type == expected_type
        
        # Check if the log contains the type information
        log_output = log_capture.getvalue()
        assert f"Variable type: {expected_type}" in log_output
        
        # Clear the log capture for the next iteration
        log_capture.truncate(0)
        log_capture.seek(0)

def test_log_variable_type_custom_object():
    # Create a custom class
    class CustomClass:
        pass
    
    # Redirect logging to capture output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    # Test custom object
    custom_obj = CustomClass()
    returned_type = log_variable_type(custom_obj)
    
    assert returned_type == 'CustomClass'
    log_output = log_capture.getvalue()
    assert "Variable type: CustomClass" in log_output