import pytest
import logging
import json
from src.json_logger import log_json

class MockLogger:
    def __init__(self):
        self.logs = []
    
    def log(self, level, message):
        self.logs.append((level, message))
    
    def get_last_log(self):
        return self.logs[-1] if self.logs else None

def test_log_json_basic():
    mock_logger = MockLogger()
    test_dict = {"key": "value", "number": 42}
    
    log_json(mock_logger, logging.INFO, "Test Log", test_dict)
    
    assert mock_logger.logs
    _, log_message = mock_logger.get_last_log()
    
    # Check if the log contains the original message
    assert "Test Log" in log_message
    
    # Check if log contains the formatted JSON
    assert json.dumps(test_dict, indent=2) in log_message

def test_log_json_custom_indent():
    mock_logger = MockLogger()
    test_dict = {"key": "value", "number": 42}
    
    log_json(mock_logger, logging.DEBUG, "Custom Indent", test_dict, indent=4)
    
    assert mock_logger.logs
    _, log_message = mock_logger.get_last_log()
    
    # Check if the log uses 4-space indentation
    assert json.dumps(test_dict, indent=4) in log_message

def test_json_logger_invalid_input():
    mock_logger = MockLogger()
    
    # Test non-dictionary input
    with pytest.raises(TypeError):
        log_json(mock_logger, logging.INFO, "Invalid Input", "Not a dict")
    
    # Test negative indent
    with pytest.raises(ValueError):
        log_json(mock_logger, logging.INFO, "Invalid Indent", {"key": "value"}, indent=-1)

def test_log_json_nested_dict():
    mock_logger = MockLogger()
    test_dict = {
        "user": {
            "name": "John",
            "details": {
                "age": 30,
                "city": "New York"
            }
        }
    }
    
    log_json(mock_logger, logging.INFO, "Nested Dict", test_dict)
    
    assert mock_logger.logs
    _, log_message = mock_logger.get_last_log()
    
    # Verify nested structure is preserved
    assert json.dumps(test_dict, indent=2) in log_message