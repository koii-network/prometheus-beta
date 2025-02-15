import pytest
import logging
from src.variable_type_logger import log_variable_type

def test_log_variable_type(caplog):
    # Test various types of variables
    test_cases = [
        (42, 'int'),
        (3.14, 'float'),
        ('hello', 'str'),
        ([1, 2, 3], 'list'),
        ({'a': 1}, 'dict'),
        ((1, 2), 'tuple'),
        (None, 'NoneType'),
        (True, 'bool'),
    ]
    
    for variable, expected_type in test_cases:
        # Clear previous log records
        caplog.clear()
        
        # Call the function
        result = log_variable_type(variable)
        
        # Check the return value
        assert result == expected_type
        
        # Check logging
        assert len(caplog.records) == 1
        assert caplog.records[0].levelname == 'INFO'
        assert f"Variable type: {expected_type}" in caplog.records[0].message

def test_log_variable_type_custom_class():
    # Test with a custom class
    class CustomClass:
        pass
    
    custom_obj = CustomClass()
    
    caplog.clear()
    result = log_variable_type(custom_obj)
    
    assert result == 'CustomClass'
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == 'INFO'
    assert "Variable type: CustomClass" in caplog.records[0].message