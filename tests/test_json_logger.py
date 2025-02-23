import pytest
import logging
import json
from src.json_logger import log_json

class MockLogger:
    def __init__(self):
        self.logs = {
            'debug': [],
            'info': [],
            'warning': [],
            'error': [],
            'critical': []
        }

    def debug(self, msg):
        self.logs['debug'].append(msg)

    def info(self, msg):
        self.logs['info'].append(msg)

    def warning(self, msg):
        self.logs['warning'].append(msg)

    def error(self, msg):
        self.logs['error'].append(msg)

    def critical(self, msg):
        self.logs['critical'].append(msg)

def test_log_json_default():
    logger = MockLogger()
    test_obj = {"key": "value", "nested": {"inner_key": "inner_value"}}
    
    log_json(logger, test_obj)
    
    # Verify the log was added to info logs
    assert len(logger.logs['info']) == 1
    logged_msg = logger.logs['info'][0]
    
    # Verify JSON formatting
    parsed_log = json.loads(logged_msg)
    assert parsed_log == test_obj

def test_log_json_with_message():
    logger = MockLogger()
    test_obj = {"key": "value"}
    
    log_json(logger, test_obj, message="Test Log")
    
    # Verify the log starts with the message
    assert logger.logs['info'][0].startswith("Test Log")

def test_log_json_different_levels():
    logger = MockLogger()
    test_obj = {"key": "value"}
    
    # Test all log levels
    levels = ['debug', 'info', 'warning', 'error', 'critical']
    for level in levels:
        log_json(logger, test_obj, log_level=level)
    
    # Verify a log was added to each level
    for level in levels:
        assert len(logger.logs[level]) == 1

def test_log_json_invalid_type():
    logger = MockLogger()
    
    # Should raise TypeError for non-dict input
    with pytest.raises(TypeError, match="Input must be a dictionary"):
        log_json(logger, "not a dict")

def test_log_json_invalid_log_level():
    logger = MockLogger()
    
    # Should raise ValueError for invalid log level
    with pytest.raises(ValueError, match="Invalid log level"):
        log_json(logger, {"key": "value"}, log_level="invalid_level")