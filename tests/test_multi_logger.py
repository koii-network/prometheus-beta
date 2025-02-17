import logging
import pytest
from src.multi_logger import log_multiple

class MockLogger:
    def __init__(self):
        self.debug_messages = []
        self.info_messages = []
        self.warning_messages = []
        self.error_messages = []
        self.critical_messages = []
    
    def debug(self, message):
        self.debug_messages.append(message)
    
    def info(self, message):
        self.info_messages.append(message)
    
    def warning(self, message):
        self.warning_messages.append(message)
    
    def error(self, message):
        self.error_messages.append(message)
    
    def critical(self, message):
        self.critical_messages.append(message)

def test_log_multiple_single_value():
    mock_logger = MockLogger()
    log_multiple(logging.INFO, "Hello", logger=mock_logger)
    assert len(mock_logger.info_messages) == 1
    assert mock_logger.info_messages[0] == "Hello"

def test_log_multiple_multiple_values():
    mock_logger = MockLogger()
    log_multiple(logging.INFO, "User", 42, "logged in", logger=mock_logger)
    assert len(mock_logger.info_messages) == 1
    assert mock_logger.info_messages[0] == "User 42 logged in"

def test_log_multiple_different_levels():
    mock_logger = MockLogger()
    log_multiple(logging.DEBUG, "Debug message", logger=mock_logger)
    log_multiple(logging.WARNING, "Warning", "message", logger=mock_logger)
    log_multiple(logging.ERROR, "Error", 500, logger=mock_logger)
    
    assert len(mock_logger.debug_messages) == 1
    assert len(mock_logger.warning_messages) == 1
    assert len(mock_logger.error_messages) == 1

def test_log_multiple_mixed_types():
    mock_logger = MockLogger()
    log_multiple(logging.INFO, "Value:", 42, "Status:", True, logger=mock_logger)
    assert mock_logger.info_messages[0] == "Value: 42 Status: True"

def test_invalid_log_level():
    with pytest.raises(ValueError):
        log_multiple(99, "Invalid log level", logger=logging.getLogger())