import pytest
import logging
import io
import sys

from src.error_logger import log_error

class TestErrorLogger:
    def test_default_error_logging(self, caplog):
        """
        Test logging with default error message
        """
        @log_error()
        def raising_function():
            raise ValueError("Test error")
        
        # Capture the log output
        with pytest.raises(ValueError):
            raising_function()
        
        # Check that the log contains the expected information
        assert "Error in function raising_function" in caplog.text
        assert "Test error" in caplog.text

    def test_custom_error_logging(self, caplog):
        """
        Test logging with a custom error message
        """
        @log_error("Custom error occurred")
        def another_raising_function():
            raise RuntimeError("Specific error")
        
        # Capture the log output
        with pytest.raises(RuntimeError):
            another_raising_function()
        
        # Check that the log contains the custom message
        assert "Custom error occurred" in caplog.text
        assert "Specific error" in caplog.text

    def test_no_error_case(self):
        """
        Test that function works normally when no error occurs
        """
        @log_error("This should not be logged")
        def successful_function():
            return "Success"
        
        result = successful_function()
        assert result == "Success"

    def test_preserves_function_metadata(self):
        """
        Test that function metadata is preserved
        """
        @log_error()
        def example_function(x, y):
            """A docstring"""
            return x + y
        
        assert example_function.__name__ == "example_function"
        assert example_function.__doc__ == "A docstring"
        assert example_function(2, 3) == 5