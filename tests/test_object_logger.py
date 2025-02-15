import pytest
import logging
from src.object_logger import log_object_details

def test_log_object_details(caplog):
    # Test logging of a simple dictionary
    test_dict = {"name": "John", "age": 30, "city": "New York"}
    
    # Set the logging level to INFO to capture the logs
    caplog.set_level(logging.INFO)
    
    # Call the function
    log_object_details(test_dict)
    
    # Check total number of keys
    assert "Total number of keys: 3" in caplog.text
    
    # Check individual key-value pairs
    assert "Key: name, Value: John" in caplog.text
    assert "Key: age, Value: 30" in caplog.text
    assert "Key: city, Value: New York" in caplog.text

def test_log_object_details_empty_dict(caplog):
    # Test logging of an empty dictionary
    caplog.set_level(logging.INFO)
    
    log_object_details({})
    
    assert "Total number of keys: 0" in caplog.text

def test_log_object_details_invalid_input():
    # Test that TypeError is raised for non-dictionary input
    with pytest.raises(TypeError, match="Input must be a dictionary"):
        log_object_details("not a dictionary")
        log_object_details(123)
        log_object_details(None)