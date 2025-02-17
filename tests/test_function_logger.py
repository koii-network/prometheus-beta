import pytest
import logging
import io
from src.function_logger import log_execution

# Capture log output
def test_log_execution():
    # Capture log output
    log_capture = io.StringIO()
    logger = logging.getLogger()
    handler = logging.StreamHandler(log_capture)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    # Test function to be decorated
    @log_execution(logger=logger)
    def sample_function(a, b):
        return a + b

    # Call the decorated function
    result = sample_function(3, 4)
    
    # Check result
    assert result == 7
    
    # Get log output
    log_output = log_capture.getvalue()
    
    # Check log output contains expected messages
    assert "Executing function: sample_function" in log_output
    assert "Arguments: args=(3, 4), kwargs={}" in log_output
    assert "Function sample_function completed successfully" in log_output
    assert "Execution time:" in log_output

def test_log_execution_exception():
    # Capture log output
    log_capture = io.StringIO()
    logger = logging.getLogger()
    handler = logging.StreamHandler(log_capture)
    logger.addHandler(handler)
    logger.setLevel(logging.ERROR)

    # Test function that raises an exception
    @log_execution(logger=logger)
    def error_function():
        raise ValueError("Test error")

    # Check that the exception is raised
    with pytest.raises(ValueError, match="Test error"):
        error_function()

    # Get log output
    log_output = log_capture.getvalue()
    
    # Check log output contains error message
    assert "Exception in error_function: Test error" in log_output