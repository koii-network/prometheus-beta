import pytest
import logging
import json
from src.json_logger import log_json_object

# Create a mock logger for testing
class MockLogger:
    def __init__(self):
        self.debug_messages = []
        self.info_messages = []
        self.warning_messages = []
        self.error_messages = []
        self.critical_messages = []
    
    def debug(self, msg):
        self.debug_messages.append(msg)
    
    def info(self, msg):
        self.info_messages.append(msg)
    
    def warning(self, msg):
        self.warning_messages.append(msg)
    
    def error(self, msg):
        self.error_messages.append(msg)
    
    def critical(self, msg):
        self.critical_messages.append(msg)

def test_log_json_object_basic():
    # Test basic logging of a JSON object
    logger = MockLogger()
    test_dict = {"key1": "value1", "key2": 42}
    
    result = log_json_object(logger, logging.INFO, test_dict)
    
    assert len(logger.info_messages) == 1
    assert json.loads(result) == test_dict
    assert "key1" in logger.info_messages[0]
    assert "value1" in logger.info_messages[0]

def test_log_json_object_with_message():
    # Test logging with an additional message
    logger = MockLogger()
    test_dict = {"key1": "value1"}
    
    result = log_json_object(logger, logging.DEBUG, test_dict, "Test message")
    
    assert len(logger.debug_messages) == 1
    assert "Test message" in logger.debug_messages[0]
    assert json.loads(result) == test_dict

def test_log_json_object_different_levels():
    # Test logging at different levels
    logger = MockLogger()
    test_dict = {"key1": "value1"}
    
    levels = [
        (logging.DEBUG, logger.debug_messages),
        (logging.INFO, logger.info_messages),
        (logging.WARNING, logger.warning_messages),
        (logging.ERROR, logger.error_messages),
        (logging.CRITICAL, logger.critical_messages)
    ]
    
    for level, message_list in levels:
        log_json_object(logger, level, test_dict)
        assert len(message_list) > 0

def test_log_json_object_invalid_input():
    # Test invalid input types
    logger = MockLogger()
    
    # Test non-dictionary input
    with pytest.raises(ValueError, match="Input must be a dictionary"):
        log_json_object(logger, logging.INFO, "not a dict")
    
    # Test invalid log level
    with pytest.raises(ValueError, match="Invalid log level"):
        log_json_object(logger, 999, {"key": "value"})