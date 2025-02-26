import pytest
import logging
from src.variable_type_logger import log_variable_type

def test_log_variable_type_with_different_types(caplog):
    # Test various types of variables
    test_cases = [
        (42, 'int'),
        (3.14, 'float'),
        ('hello', 'str'),
        ([1, 2, 3], 'list'),
        ({'a': 1}, 'dict'),
        ((1, 2), 'tuple'),
        (None, 'NoneType'),
        (True, 'bool')
    ]
    
    for variable, expected_type in test_cases:
        # Clear previous log records
        caplog.clear()
        
        # Call the function
        result = log_variable_type(variable)
        
        # Assert the return value matches the type
        assert result == expected_type
        
        # Assert logging occurred with correct message
        assert len(caplog.records) == 1
        assert caplog.records[0].levelname == 'INFO'
        assert f"Variable type: {expected_type}" in caplog.records[0].message

def test_log_variable_type_custom_class():
    # Define a custom class
    class CustomClass:
        pass
    
    # Create an instance of the custom class
    custom_obj = CustomClass()
    
    # Call the function and check the logging
    result = log_variable_type(custom_obj)
    assert result == 'CustomClass'

def test_log_variable_type_no_arguments():
    with pytest.raises(TypeError):
        log_variable_type()