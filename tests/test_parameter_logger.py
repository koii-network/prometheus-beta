import logging
import pytest
from src.parameter_logger import log_parameters

# Create a custom logger for testing
class MockLogger:
    def __init__(self):
        self.logged_messages = []
    
    def info(self, message):
        self.logged_messages.append(message)

def test_log_parameters_basic():
    """Test basic parameter logging functionality"""
    mock_logger = MockLogger()
    
    @log_parameters(logger=mock_logger)
    def test_func(a, b, c=10):
        return a + b + c
    
    # Call the function
    result = test_func(1, 2, c=3)
    
    # Check the result
    assert result == 6
    
    # Check logging
    assert len(mock_logger.logged_messages) == 1
    assert "test_func" in mock_logger.logged_messages[0]
    assert "{'a': 1, 'b': 2, 'c': 3}" in mock_logger.logged_messages[0]

def test_log_parameters_with_defaults():
    """Test logging with default parameters"""
    mock_logger = MockLogger()
    
    @log_parameters(logger=mock_logger)
    def test_func(a, b=5, c=10):
        return a + b + c
    
    # Call the function with partial arguments
    result = test_func(1)
    
    # Check the result
    assert result == 16
    
    # Check logging
    assert len(mock_logger.logged_messages) == 1
    assert "test_func" in mock_logger.logged_messages[0]
    assert "{'a': 1, 'b': 5, 'c': 10}" in mock_logger.logged_messages[0]

def test_log_parameters_no_logger():
    """Test logging with default (root) logger"""
    # Capture log messages
    log_capture = []
    root_logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    
    # Temporarily add a capture handler
    root_logger.addHandler(handler)
    handler.setLevel(logging.INFO)
    
    @log_parameters()
    def test_func(x, y):
        return x + y
    
    # Redirect log output to our list
    try:
        with pytest.MonkeyPatch.context() as m:
            m.setattr(handler, 'emit', lambda record: log_capture.append(handler.format(record)))
            
            # Call the function
            result = test_func(3, 4)
            
            # Check the result
            assert result == 7
            
            # Check logging
            assert len(log_capture) > 0
            assert "test_func" in log_capture[0]
            assert "{'x': 3, 'y': 4}" in log_capture[0]
    finally:
        # Remove the handler
        root_logger.removeHandler(handler)

def test_log_parameters_multiple_calls():
    """Test logging across multiple function calls"""
    mock_logger = MockLogger()
    
    @log_parameters(logger=mock_logger)
    def test_func(a, b):
        return a * b
    
    # Multiple calls
    test_func(2, 3)
    test_func(4, 5)
    
    # Check logging
    assert len(mock_logger.logged_messages) == 2
    assert "{'a': 2, 'b': 3}" in mock_logger.logged_messages[0]
    assert "{'a': 4, 'b': 5}" in mock_logger.logged_messages[1]