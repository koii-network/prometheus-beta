import logging
import pytest
from src.function_logger import log_execution

# Create a logger for testing
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class TestFunctionLogger:
    def test_basic_logging(self, caplog):
        """Test basic logging functionality"""
        caplog.set_level(logging.INFO)
        
        @log_execution(logger)
        def sample_function(x, y):
            return x + y
        
        result = sample_function(3, 4)
        
        assert result == 7
        assert "Starting execution of sample_function" in caplog.text
        assert "Finished execution of sample_function" in caplog.text
    
    def test_exception_logging(self, caplog):
        """Test logging of exceptions"""
        caplog.set_level(logging.ERROR)
        
        @log_execution(logger)
        def error_function():
            raise ValueError("Test error")
        
        with pytest.raises(ValueError, match="Test error"):
            error_function()
        
        assert "Exception in error_function" in caplog.text
    
    def test_default_logger(self, caplog):
        """Test logging with default logger"""
        caplog.set_level(logging.INFO)
        
        @log_execution()
        def default_logger_function():
            return "success"
        
        result = default_logger_function()
        
        assert result == "success"
        assert "Starting execution of default_logger_function" in caplog.text
        assert "Finished execution of default_logger_function" in caplog.text
    
    def test_debug_logging(self, caplog):
        """Test debug level logging"""
        caplog.set_level(logging.DEBUG)
        
        @log_execution(logger)
        def complex_function(a, b, c=10):
            return a * b + c
        
        result = complex_function(2, 3, c=5)
        
        assert result == 11
        assert "Arguments: args=(2, 3)" in caplog.text
        assert "kwargs={'c': 5}" in caplog.text
        assert "Execution time:" in caplog.text