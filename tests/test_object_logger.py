import pytest
import logging
from src.object_logger import log_object_details

# Capture log messages for testing
class LogCapture:
    def __init__(self):
        self.records = []
    
    def emit(self, record):
        self.records.append(record.getMessage())

def test_log_object_details_normal_case(caplog):
    """Test logging of a standard dictionary"""
    test_dict = {"name": "John", "age": 30}
    
    # Set log level to INFO to capture all log messages
    caplog.set_level(logging.INFO)
    
    # Call the function
    log_object_details(test_dict)
    
    # Check log messages
    log_messages = [record.message for record in caplog.records]
    assert "Object contains 2 key-value pair(s)" in log_messages
    assert "Key: name, Value: John" in log_messages
    assert "Key: age, Value: 30" in log_messages

def test_log_object_details_empty_dict():
    """Test that empty dictionary raises ValueError"""
    with pytest.raises(ValueError, match="Input dictionary cannot be empty"):
        log_object_details({})

def test_log_object_details_invalid_type():
    """Test that non-dictionary input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a dictionary"):
        log_object_details("not a dict")
    with pytest.raises(TypeError, match="Input must be a dictionary"):
        log_object_details(123)
    with pytest.raises(TypeError, match="Input must be a dictionary"):
        log_object_details(["list", "not", "dict"])

def test_log_object_details_complex_values(caplog):
    """Test logging of dictionary with complex values"""
    test_dict = {
        "nested": {"a": 1},
        "list": [1, 2, 3],
        "none": None
    }
    
    caplog.set_level(logging.INFO)
    log_object_details(test_dict)
    
    log_messages = [record.message for record in caplog.records]
    assert "Object contains 3 key-value pair(s)" in log_messages
    assert "Key: nested, Value: {'a': 1}" in log_messages
    assert "Key: list, Value: [1, 2, 3]" in log_messages
    assert "Key: none, Value: None" in log_messages