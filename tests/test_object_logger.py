import logging
import pytest
from src.object_logger import log_object_details

# Custom class for testing
class TestClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def test_log_object_details_with_dict(caplog):
    # Test logging a dictionary
    caplog.set_level(logging.INFO)
    test_dict = {"name": "John", "age": 30}
    
    result = log_object_details(test_dict)
    
    assert result == 2
    assert "Logging details for dict" in caplog.text
    assert "name: John" in caplog.text
    assert "age: 30" in caplog.text

def test_log_object_details_with_object(caplog):
    # Test logging an object
    caplog.set_level(logging.INFO)
    test_obj = TestClass("Alice", 25)
    
    result = log_object_details(test_obj)
    
    assert result == 2
    assert "Logging details for TestClass" in caplog.text
    assert "name: Alice" in caplog.text
    assert "age: 25" in caplog.text

def test_log_object_details_with_invalid_input():
    # Test raising TypeError for invalid input
    with pytest.raises(TypeError, match="Input must be a dictionary or an object with __dict__"):
        log_object_details("not a dict or object")

def test_log_object_details_with_custom_logger(caplog):
    # Create a custom logger
    custom_logger = logging.getLogger('custom_logger')
    custom_logger.setLevel(logging.INFO)
    
    test_dict = {"key": "value"}
    
    result = log_object_details(test_dict, logger=custom_logger)
    
    assert result == 1
    assert "key: value" in caplog.text