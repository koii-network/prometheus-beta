import logging
import pytest
from src.object_logger import log_object

class MockLogger:
    def __init__(self):
        self.log_messages = []
        self.error_messages = []
    
    def log(self, level, msg):
        self.log_messages.append((level, msg))
    
    def error(self, msg):
        self.error_messages.append(msg)

def test_log_simple_dict():
    # Test logging a simple dictionary
    mock_logger = MockLogger()
    test_dict = {"name": "John", "age": 30}
    
    result = log_object(test_dict, logger=mock_logger)
    
    assert len(mock_logger.log_messages) == 1
    assert 'John' in result
    assert '30' in result

def test_log_nested_dict():
    # Test logging a nested dictionary
    mock_logger = MockLogger()
    test_dict = {
        "user": {
            "name": "Alice", 
            "details": {"age": 25, "city": "New York"}
        }
    }
    
    result = log_object(test_dict, logger=mock_logger)
    
    assert len(mock_logger.log_messages) == 1
    assert 'Alice' in result
    assert 'New York' in result

def test_log_list():
    # Test logging a list
    mock_logger = MockLogger()
    test_list = [1, 2, 3, {"a": 1, "b": 2}]
    
    result = log_object(test_list, logger=mock_logger)
    
    assert len(mock_logger.log_messages) == 1
    assert '1' in result
    assert '2' in result

def test_log_custom_log_level():
    # Test logging with a custom log level
    mock_logger = MockLogger()
    test_obj = {"key": "value"}
    
    result = log_object(test_obj, log_level=logging.DEBUG, logger=mock_logger)
    
    assert len(mock_logger.log_messages) == 1
    assert mock_logger.log_messages[0][0] == logging.DEBUG

def test_unhashable_object():
    # Test logging an unhashable object
    mock_logger = MockLogger()
    
    # Use a lambda function as an unhashable object
    result = log_object(lambda x: x, logger=mock_logger)
    
    assert len(mock_logger.log_messages) == 1
    assert 'lambda' in result

def test_recursive_object():
    # Test logging a recursive object
    mock_logger = MockLogger()
    
    recursive_dict = {"self": None}
    recursive_dict["self"] = recursive_dict
    
    result = log_object(recursive_dict, logger=mock_logger)
    
    assert len(mock_logger.log_messages) == 1
    assert '<Recursion on dict' in result