import pytest
import logging
from src.object_logger import log_object

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

def test_log_object_simple():
    """Test logging a simple object"""
    mock_logger = MockLogger()
    obj = {"name": "John", "age": 30}
    result = log_object(obj, logger=mock_logger)
    
    assert len(mock_logger.logs['info']) == 1
    assert "John" in result
    assert "30" in result

def test_log_object_complex():
    """Test logging a complex nested object"""
    mock_logger = MockLogger()
    obj = {
        "users": [
            {"name": "Alice", "details": {"age": 25, "city": "New York"}},
            {"name": "Bob", "details": {"age": 35, "city": "San Francisco"}}
        ]
    }
    result = log_object(obj, logger=mock_logger)
    
    assert len(mock_logger.logs['info']) == 1
    assert "Alice" in result
    assert "New York" in result
    assert "San Francisco" in result

def test_log_object_different_levels():
    """Test logging at different log levels"""
    mock_logger = MockLogger()
    levels = ['debug', 'warning', 'error', 'critical']
    obj = {"test": "level_check"}
    
    for level in levels:
        log_object(obj, log_level=level, logger=mock_logger)
        assert len(getattr(mock_logger.logs, level)) == 1

def test_log_object_invalid_level():
    """Test that an invalid log level raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid log level"):
        log_object({"test": "invalid"}, log_level="invalid_level")

def test_log_object_empty():
    """Test logging an empty object"""
    mock_logger = MockLogger()
    obj = {}
    result = log_object(obj, logger=mock_logger)
    
    assert len(mock_logger.logs['info']) == 1
    assert result == "{}"