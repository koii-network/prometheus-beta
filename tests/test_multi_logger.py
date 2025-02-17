import logging
import pytest
from src.multi_logger import log_multiple

class MockLogger:
    def __init__(self):
        self.messages = {
            logging.DEBUG: [],
            logging.INFO: [],
            logging.WARNING: [],
            logging.ERROR: [],
            logging.CRITICAL: []
        }
    
    def debug(self, message):
        self.messages[logging.DEBUG].append(message)
    
    def info(self, message):
        self.messages[logging.INFO].append(message)
    
    def warning(self, message):
        self.messages[logging.WARNING].append(message)
    
    def error(self, message):
        self.messages[logging.ERROR].append(message)
    
    def critical(self, message):
        self.messages[logging.CRITICAL].append(message)

def test_log_multiple_single_value():
    mock_logger = MockLogger()
    log_multiple(logging.INFO, "Test message", logger=mock_logger)
    assert mock_logger.messages[logging.INFO] == ["Test message"]

def test_log_multiple_multiple_values():
    mock_logger = MockLogger()
    log_multiple(logging.DEBUG, "Value1", 42, 3.14, logger=mock_logger)
    assert mock_logger.messages[logging.DEBUG] == ["Value1 42 3.14"]

def test_log_multiple_different_types():
    mock_logger = MockLogger()
    log_multiple(logging.WARNING, "String", 123, ["list"], {"key": "value"}, logger=mock_logger)
    assert mock_logger.messages[logging.WARNING] == ["String 123 ['list'] {'key': 'value'}"]

def test_log_multiple_all_log_levels():
    mock_logger = MockLogger()
    
    log_multiple(logging.DEBUG, "Debug message", logger=mock_logger)
    log_multiple(logging.INFO, "Info message", logger=mock_logger)
    log_multiple(logging.WARNING, "Warning message", logger=mock_logger)
    log_multiple(logging.ERROR, "Error message", logger=mock_logger)
    log_multiple(logging.CRITICAL, "Critical message", logger=mock_logger)
    
    assert mock_logger.messages[logging.DEBUG] == ["Debug message"]
    assert mock_logger.messages[logging.INFO] == ["Info message"]
    assert mock_logger.messages[logging.WARNING] == ["Warning message"]
    assert mock_logger.messages[logging.ERROR] == ["Error message"]
    assert mock_logger.messages[logging.CRITICAL] == ["Critical message"]

def test_log_multiple_invalid_level():
    mock_logger = MockLogger()
    with pytest.raises(ValueError, match="Unsupported logging level"):
        log_multiple(99, "Invalid level", logger=mock_logger)