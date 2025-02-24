"""
Unit tests for the JSON logging function.
"""

import json
import logging
import pytest

from src.json_logger import log_json


class MockLogger:
    """
    Mock logger to capture log messages for testing.
    """
    def __init__(self):
        self.logged_messages = []
        self.logged_levels = []

    def log(self, level, msg):
        self.logged_messages.append(msg)
        self.logged_levels.append(level)


def test_basic_json_logging():
    """Test logging a simple dictionary."""
    mock_logger = MockLogger()
    data = {"name": "John", "age": 30}
    
    result = log_json(data, logger=mock_logger)
    
    # Check the logged message matches JSON dump
    assert mock_logger.logged_messages[0] == json.dumps(data, indent=2)
    assert mock_logger.logged_levels[0] == logging.INFO
    assert result == json.dumps(data, indent=2)


def test_custom_indent():
    """Test logging with custom indentation."""
    mock_logger = MockLogger()
    data = {"items": [1, 2, 3]}
    
    result = log_json(data, indent=4, logger=mock_logger)
    
    # Check the logged message matches JSON dump with 4-space indent
    assert mock_logger.logged_messages[0] == json.dumps(data, indent=4)
    assert result == json.dumps(data, indent=4)


def test_nested_json():
    """Test logging a nested dictionary."""
    mock_logger = MockLogger()
    data = {
        "user": {
            "name": "Alice",
            "details": {
                "age": 25,
                "city": "New York"
            }
        }
    }
    
    result = log_json(data, logger=mock_logger)
    
    # Check the logged message matches JSON dump
    assert mock_logger.logged_messages[0] == json.dumps(data, indent=2)
    assert result == json.dumps(data, indent=2)


def test_invalid_json_raises_error():
    """Test that non-serializable objects raise a TypeError."""
    mock_logger = MockLogger()
    
    # Create a non-serializable object (function)
    non_serializable_data = {"func": lambda x: x}
    
    with pytest.raises(TypeError):
        log_json(non_serializable_data, logger=mock_logger)


def test_negative_indent_raises_error():
    """Test that negative indent raises a ValueError."""
    mock_logger = MockLogger()
    data = {"key": "value"}
    
    with pytest.raises(ValueError, match="Indent must be a non-negative integer"):
        log_json(data, indent=-1, logger=mock_logger)


def test_log_level_selection():
    """Test logging with different log levels."""
    mock_logger = MockLogger()
    data = {"status": "active"}
    
    log_json(data, log_level=logging.WARNING, logger=mock_logger)
    
    assert mock_logger.logged_levels[0] == logging.WARNING


def test_empty_dict():
    """Test logging an empty dictionary."""
    mock_logger = MockLogger()
    data = {}
    
    result = log_json(data, logger=mock_logger)
    
    assert mock_logger.logged_messages[0] == '{}'
    assert result == '{}'