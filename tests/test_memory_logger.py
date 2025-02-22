import logging
import memory_profiler
import pytest
from src.memory_logger import log_memory_usage

# Configure logging for tests
logging.basicConfig(level=logging.INFO)

class TestMemoryLogger:
    def test_log_memory_usage_decorator(self, caplog):
        # Create a simple function to test memory logging
        @log_memory_usage()
        def sample_function():
            # Allocate some memory
            large_list = [i for i in range(100000)]
            return len(large_list)
        
        # Capture log records
        caplog.set_level(logging.INFO)
        
        # Call the decorated function
        result = sample_function()
        
        # Check function return value
        assert result == 100000
        
        # Check log messages
        log_records = caplog.records
        assert len(log_records) == 3  # Before, After, and Difference logs
        
        # Verify log messages contain expected information
        log_messages = [record.getMessage() for record in log_records]
        assert any("Memory usage before sample_function" in msg for msg in log_messages)
        assert any("Memory usage after sample_function" in msg for msg in log_messages)
        assert any("Memory usage change in sample_function" in msg for msg in log_messages)
    
    def test_log_memory_usage_with_custom_logger(self):
        # Create a custom logger
        custom_logger = logging.getLogger('custom_logger')
        custom_logger.setLevel(logging.INFO)
        log_handler = logging.StreamHandler()
        custom_logger.addHandler(log_handler)
        
        # Decorator with custom logger
        @log_memory_usage(logger=custom_logger)
        def another_function():
            return sum(range(10000))
        
        # Call the function
        result = another_function()
        assert result == 49995000
    
    def test_log_memory_usage_exception(self):
        @log_memory_usage()
        def error_function():
            raise ValueError("Test error")
        
        # Expect the original exception to be raised
        with pytest.raises(ValueError, match="Test error"):
            error_function()