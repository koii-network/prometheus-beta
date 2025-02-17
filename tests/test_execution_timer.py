import pytest
import logging
import time
from src.execution_timer import log_execution_time

# Configure logging
logging.basicConfig(level=logging.INFO)

def test_log_execution_time_default_logger(caplog):
    @log_execution_time()
    def sample_function(x, y):
        time.sleep(0.1)  # Simulate some work
        return x + y
    
    caplog.set_level(logging.INFO)
    result = sample_function(3, 4)
    
    assert result == 7
    assert "Function 'sample_function' took" in caplog.text
    assert "seconds to execute" in caplog.text

def test_log_execution_time_custom_logger(caplog):
    # Create a custom logger
    custom_logger = logging.getLogger('test_logger')
    custom_logger.setLevel(logging.INFO)
    
    @log_execution_time(logger=custom_logger)
    def another_function():
        time.sleep(0.05)  # Simulate some work
        return "done"
    
    # Use a handler to capture log messages
    handler = logging.StreamHandler()
    custom_logger.addHandler(handler)
    
    result = another_function()
    
    assert result == "done"
    
    # Check log messages
    log_records = [record for record in caplog.records if record.name == 'test_logger']
    assert len(log_records) > 0
    assert "Function 'another_function' took" in log_records[0].message

def test_log_execution_time_exception(caplog):
    @log_execution_time()
    def function_with_error():
        raise ValueError("Test error")
    
    caplog.set_level(logging.ERROR)
    
    with pytest.raises(ValueError, match="Test error"):
        function_with_error()
    
    assert "Error in function 'function_with_error'" in caplog.text