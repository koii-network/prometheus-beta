import pytest
import logging
import json
from src.json_logger import log_json

# Create a custom logger for testing
class MockLogger:
    def __init__(self):
        self.logged_messages = []
    
    def log(self, level, message):
        self.logged_messages.append((level, message))

def test_log_json_basic():
    logger = MockLogger()
    test_dict = {"key": "value", "number": 42}
    
    log_json(logger, logging.INFO, test_dict)
    
    assert len(logger.logged_messages) == 1
    level, message = logger.logged_messages[0]
    assert level == logging.INFO
    assert json.loads(message) == test_dict

def test_log_json_with_message():
    logger = MockLogger()
    test_dict = {"key": "value", "number": 42}
    
    log_json(logger, logging.DEBUG, test_dict, "Test message")
    
    assert len(logger.logged_messages) == 1
    level, message = logger.logged_messages[0]
    assert level == logging.DEBUG
    assert "Test message" in message
    assert json.loads(message.split('\\n')[1]) == test_dict

def test_log_json_invalid_logger():
    with pytest.raises(TypeError, match="Invalid logger object"):
        log_json("not a logger", logging.INFO, {})

def test_log_json_invalid_json_obj():
    logger = MockLogger()
    
    with pytest.raises(TypeError, match="json_obj must be a dictionary or list"):
        log_json(logger, logging.INFO, "not a dict")

def test_log_json_non_serializable():
    logger = MockLogger()
    
    # Create an object that can't be JSON serialized
    class NonSerializable:
        pass
    
    with pytest.raises(TypeError, match="Unable to serialize JSON"):
        log_json(logger, logging.INFO, {"obj": NonSerializable()})