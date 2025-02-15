import logging
import pytest
from src.multiline_logger import log_multiline

class MockLogger:
    def __init__(self):
        self.logs = []

    def log(self, level, message):
        self.logs.append((level, message))

def test_log_multiline_default():
    mock_logger = MockLogger()
    message = "Test multiline\nlog message"
    
    log_multiline(message, logger=mock_logger)
    
    assert len(mock_logger.logs) == 3
    assert mock_logger.logs[0][0] == logging.INFO
    assert mock_logger.logs[1][0] == logging.INFO
    assert mock_logger.logs[2][0] == logging.INFO
    assert mock_logger.logs[0][1].startswith('=' * 40)
    assert mock_logger.logs[1][1] == message
    assert mock_logger.logs[2][1].startswith('=' * 40)

def test_log_multiline_custom_separator():
    mock_logger = MockLogger()
    message = "Custom separator test"
    
    log_multiline(message, logger=mock_logger, separator='-', separator_length=20)
    
    assert len(mock_logger.logs) == 3
    assert mock_logger.logs[0][1] == '-' * 20
    assert mock_logger.logs[1][1] == message
    assert mock_logger.logs[2][1] == '-' * 20

def test_log_multiline_custom_level():
    mock_logger = MockLogger()
    message = "Custom log level test"
    
    log_multiline(message, logger=mock_logger, level=logging.WARNING)
    
    assert len(mock_logger.logs) == 3
    assert all(log[0] == logging.WARNING for log in mock_logger.logs)