import pytest
import logging
from src.object_logger import log_object_details

def test_log_object_details(caplog):
    # Test logging of a non-empty dictionary
    caplog.set_level(logging.INFO)
    test_dict = {"name": "John", "age": 30, "city": "New York"}
    log_object_details(test_dict)
    
    # Check log messages
    assert "Key: name, Value: John" in caplog.text
    assert "Key: age, Value: 30" in caplog.text
    assert "Key: city, Value: New York" in caplog.text

def test_empty_dictionary(caplog):
    # Test logging of an empty dictionary
    caplog.set_level(logging.INFO)
    log_object_details({})
    
    # Check log message for empty dictionary
    assert "The object is empty (no keys or values)" in caplog.text

def test_invalid_input():
    # Test raising TypeError for non-dictionary input
    with pytest.raises(TypeError, match="Input must be a dictionary"):
        log_object_details("not a dictionary")
    
    with pytest.raises(TypeError, match="Input must be a dictionary"):
        log_object_details(None)
    
    with pytest.raises(TypeError, match="Input must be a dictionary"):
        log_object_details(123)