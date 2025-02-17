import pytest
import logging
from src.type_logger import log_variable_type

def test_log_variable_type(caplog):
    # Test with different types of variables
    test_cases = [
        (42, 'int'),
        (3.14, 'float'),
        ('hello', 'str'),
        ([1, 2, 3], 'list'),
        ({'key': 'value'}, 'dict'),
        ((1, 2), 'tuple'),
        (None, 'NoneType'),
        (True, 'bool')
    ]
    
    for variable, expected_type in test_cases:
        # Clear previous log records
        caplog.clear()
        
        # Call the function
        result = log_variable_type(variable)
        
        # Check return value
        assert result == expected_type
        
        # Check logging
        assert len(caplog.records) == 1
        assert f"Variable type: {expected_type}" in caplog.text

def test_log_variable_type_with_custom_type():
    # Define a custom class
    class CustomType:
        pass
    
    custom_obj = CustomType()
    
    # Call the function and verify
    result = log_variable_type(custom_obj)
    assert result == 'CustomType'