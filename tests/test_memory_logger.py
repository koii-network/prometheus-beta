import pytest
import logging
from io import StringIO
from src.memory_logger import log_memory_usage

class TestMemoryLogger:
    def test_memory_logger_basic(self):
        # Create a string buffer to capture log messages
        log_capture = StringIO()
        handler = logging.StreamHandler(log_capture)
        logger = logging.getLogger('test_logger')
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        
        @log_memory_usage(logger=logger)
        def test_function():
            # Allocate some memory
            return [i for i in range(10000)]
        
        # Call the decorated function
        result = test_function()
        
        # Get log messages
        log_messages = log_capture.getvalue()
        
        # Assert log messages
        assert "Before test_function: Memory usage" in log_messages
        assert "After test_function: Memory usage" in log_messages
        assert "Memory change:" in log_messages
        
        # Check result is correct
        assert len(result) == 10000
        
        # Reset logging
        logger.removeHandler(handler)
    
    def test_memory_logger_default_logger(self):
        @log_memory_usage()
        def another_test_function():
            # Do something simple
            return sum(range(1000))
        
        # This should not raise any exceptions
        result = another_test_function()
        assert result == 499500
    
    def test_memory_logger_with_exception(self):
        @log_memory_usage()
        def function_with_error():
            raise ValueError("Test error")
        
        # Ensure the decorator doesn't suppress exceptions
        with pytest.raises(ValueError, match="Test error"):
            function_with_error()