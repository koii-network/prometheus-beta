import pytest
import logging
import io
import logging
from src.input_validation_logger import log_input_validation

# Create a string buffer to capture log messages
def create_log_capture():
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    logger = logging.getLogger('test_logger')
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger, log_capture

def test_decorator_logs_function_name():
    # Create a log capture
    logger, log_capture = create_log_capture()
    
    # Create a test function with the decorator
    @log_input_validation(logger=logger)
    def test_func(x, y):
        return x + y
    
    # Call the function
    test_func(1, 2)
    
    # Check log contents
    log_contents = log_capture.getvalue()
    assert "Validating inputs for function: test_func" in log_contents
    assert "Input validation successful for test_func" in log_contents

def test_decorator_logs_arguments():
    # Create a log capture
    logger, log_capture = create_log_capture()
    
    # Create a test function with the decorator
    @log_input_validation(logger=logger)
    def test_func(x, y):
        return x + y
    
    # Call the function
    test_func(1, 2)
    
    # Check log contents
    log_contents = log_capture.getvalue()
    assert "Positional arguments: (1, 2)" in log_contents

def test_decorator_logs_keyword_arguments():
    # Create a log capture
    logger, log_capture = create_log_capture()
    
    # Create a test function with the decorator
    @log_input_validation(logger=logger)
    def test_func(x, y):
        return x + y
    
    # Call the function with keyword arguments
    test_func(x=1, y=2)
    
    # Check log contents
    log_contents = log_capture.getvalue()
    assert "Keyword arguments: {'x': 1, 'y': 2}" in log_contents

def test_decorator_logs_validation_error():
    # Create a log capture
    logger, log_capture = create_log_capture()
    
    # Create a test function with the decorator that raises a ValueError
    @log_input_validation(logger=logger)
    def test_func(x):
        if x < 0:
            raise ValueError("Value must be non-negative")
        return x
    
    # Test that the original error is still raised
    with pytest.raises(ValueError, match="Value must be non-negative"):
        test_func(-1)
    
    # Check log contents
    log_contents = log_capture.getvalue()
    assert "Input validation error" in log_contents
    assert "Value must be non-negative" in log_contents

def test_decorator_works_without_explicit_logger():
    # Test the decorator works when no logger is provided
    @log_input_validation()
    def test_func(x):
        return x
    
    # Simply ensure the function can be called without error
    result = test_func(5)
    assert result == 5