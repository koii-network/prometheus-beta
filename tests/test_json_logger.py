import json
import logging
import pytest

from src.json_logger import log_json

# Create a mock logger for testing
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

def test_log_json_with_message():
    mock_logger = MockLogger()
    test_data = {"key1": "value1", "key2": 42}
    
    result = log_json(mock_logger, logging.INFO, test_data, "Test Log")
    
    assert len(mock_logger.logs['info']) == 1
    assert "Test Log: " in mock_logger.logs['info'][0]
    assert json.loads(result) == test_data

def test_log_json_without_message():
    mock_logger = MockLogger()
    test_data = {"key1": "value1", "key2": 42}
    
    result = log_json(mock_logger, logging.DEBUG, test_data)
    
    assert len(mock_logger.logs['debug']) == 1
    assert "key1" in mock_logger.logs['debug'][0]
    assert json.loads(result) == test_data

def test_log_json_different_log_levels():
    levels = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]
    test_data = {"level": "test"}
    
    for level in levels:
        mock_logger = MockLogger()
        log_json(mock_logger, level, test_data)
        
        assert len([log for log_list in mock_logger.logs.values() for log in log_list]) == 1

def test_log_json_invalid_data():
    mock_logger = MockLogger()
    
    # Test non-serializable data
    with pytest.raises(TypeError):
        log_json(mock_logger, logging.INFO, set())

def test_log_json_invalid_log_level():
    mock_logger = MockLogger()
    
    with pytest.raises(ValueError):
        log_json(mock_logger, 999, {"key": "value"})