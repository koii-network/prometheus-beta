import pytest
import logging
from src.object_logger import log_object_details

def test_log_object_details(caplog):
    # Test logging of a simple dictionary
    caplog.set_level(logging.INFO)
    test_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
    
    # Call the function and check return value
    result = log_object_details(test_dict)
    assert result == 3  # Number of items in the dictionary
    
    # Check log messages
    log_records = caplog.records
    assert len(log_records) == 4  # Header + 3 key-value pairs
    assert 'Object Keys and Values:' in log_records[0].message
    assert 'name: John' in [record.message for record in log_records]
    assert 'age: 30' in [record.message for record in log_records]
    assert 'city: New York' in [record.message for record in log_records]

def test_log_object_details_empty_dict(caplog):
    # Test logging of an empty dictionary
    caplog.set_level(logging.INFO)
    test_dict = {}
    
    # Call the function and check return value
    result = log_object_details(test_dict)
    assert result == 0  # No items in the dictionary
    
    # Check log messages
    log_records = caplog.records
    assert len(log_records) == 1
    assert 'Object Keys and Values:' in log_records[0].message

def test_log_object_details_invalid_input():
    # Test error handling for non-dictionary input
    with pytest.raises(TypeError, match="Input must be a dictionary"):
        log_object_details("not a dictionary")
    
    with pytest.raises(TypeError, match="Input must be a dictionary"):
        log_object_details(123)
    
    with pytest.raises(TypeError, match="Input must be a dictionary"):
        log_object_details(None)