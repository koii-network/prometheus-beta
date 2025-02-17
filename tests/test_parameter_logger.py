import logging
import pytest
from src.parameter_logger import log_parameters

# Set up a custom logger for testing
class MockLogger:
    def __init__(self):
        self.logs = []
    
    def info(self, message):
        self.logs.append(message)

def test_log_parameters_basic():
    # Create a mock logger
    mock_logger = MockLogger()
    
    # Create a sample function with the decorator
    @log_parameters(logger=mock_logger)
    def sample_function(a, b, c=10):
        return a + b + c
    
    # Call the function
    result = sample_function(5, 7)
    
    # Check the result
    assert result == 22
    
    # Check the logged parameters
    assert len(mock_logger.logs) == 1
    log_message = mock_logger.logs[0]
    assert "Calling sample_function with parameters:" in log_message
    assert "a: 5" in log_message
    assert "b: 7" in log_message
    assert "c: 10" in log_message

def test_log_parameters_complex_types():
    # Create a mock logger
    mock_logger = MockLogger()
    
    # Create a sample function with complex types
    @log_parameters(logger=mock_logger)
    def complex_function(lst, dct, obj=None):
        return len(lst) + len(dct)
    
    # Call the function
    result = complex_function([1,2,3], {"a": 1, "b": 2}, obj="test")
    
    # Check the result
    assert result == 5
    
    # Check the logged parameters
    assert len(mock_logger.logs) == 1
    log_message = mock_logger.logs[0]
    assert "Calling complex_function with parameters:" in log_message
    assert "lst: [1, 2, 3]" in log_message
    assert "dct: {'a': 1, 'b': 2}" in log_message
    assert "obj: 'test'" in log_message

def test_log_parameters_default_logger():
    # Capture log records
    log_capture = []
    
    # Set up a basic logging configuration
    logging.basicConfig(level=logging.INFO)
    root_logger = logging.getLogger()
    original_handlers = root_logger.handlers.copy()
    
    try:
        # Create a custom handler to capture logs
        class LogCaptureHandler(logging.Handler):
            def emit(self, record):
                log_capture.append(record.getMessage())
        
        capture_handler = LogCaptureHandler()
        root_logger.addHandler(capture_handler)
        
        # Create a sample function with default logger
        @log_parameters()
        def default_logger_function(x, y):
            return x * y
        
        # Call the function
        result = default_logger_function(4, 5)
        
        # Check the result
        assert result == 20
        
        # Check the logged parameters
        assert len(log_capture) == 1
        log_message = log_capture[0]
        assert "Calling default_logger_function with parameters:" in log_message
        assert "x: 4" in log_message
        assert "y: 5" in log_message
    
    finally:
        # Restore original handlers
        root_logger.handlers = original_handlers