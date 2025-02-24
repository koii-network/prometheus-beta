import logging
import pytest
from src.function_logger import log_function_execution

# Configure logging for tests
logging.basicConfig(level=logging.INFO)

class TestFunctionLogger:
    def test_basic_function_logging(self, caplog):
        """Test basic function logging"""
        @log_function_execution()
        def sample_function(x, y):
            return x + y
        
        caplog.set_level(logging.INFO)
        result = sample_function(3, 4)
        
        assert result == 7
        assert f"Starting execution of sample_function" in caplog.text
        assert f"Finished execution of sample_function" in caplog.text
        assert "Execution time:" in caplog.text

    def test_function_with_custom_logger(self, caplog):
        """Test logging with a custom logger"""
        # Create a custom logger
        custom_logger = logging.getLogger('test_logger')
        caplog.set_level(logging.INFO)

        @log_function_execution(logger=custom_logger)
        def another_function(x):
            return x * 2
        
        result = another_function(5)
        
        assert result == 10
        assert f"Starting execution of another_function" in caplog.text
        assert f"Finished execution of another_function" in caplog.text

    def test_function_with_exception(self, caplog):
        """Test logging when an exception occurs"""
        @log_function_execution()
        def error_function():
            raise ValueError("Test error")
        
        caplog.set_level(logging.ERROR)
        
        with pytest.raises(ValueError, match="Test error"):
            error_function()
        
        assert "Exception in error_function: Test error" in caplog.text

    def test_function_with_complex_args(self, caplog):
        """Test function with complex arguments"""
        @log_function_execution()
        def complex_args_function(a, b=None, *args, **kwargs):
            return a
        
        caplog.set_level(logging.DEBUG)
        
        result = complex_args_function(1, b=2, c=3, d=4)
        
        assert result == 1
        assert "Starting execution of complex_args_function" in caplog.text
        assert "Args:" in caplog.text
        assert "Kwargs:" in caplog.text