import logging
import pytest
from src.logging_decorator import log_execution

# Configure a test logger
test_logger = logging.getLogger('test_logger')
test_logger.setLevel(logging.INFO)

class TestLoggingDecorator:
    def test_log_execution_default_logger(self, caplog):
        @log_execution()
        def simple_function(x, y):
            return x + y
        
        caplog.set_level(logging.INFO)
        result = simple_function(3, 4)
        
        assert result == 7
        assert "Entering function: simple_function" in caplog.text
        assert "Args: (3, 4), Kwargs: {}" in caplog.text
        assert "Exiting function: simple_function" in caplog.text
    
    def test_log_execution_custom_logger(self, caplog):
        @log_execution(logger=test_logger)
        def another_function(a, b=10):
            return a * b
        
        caplog.set_level(logging.INFO)
        result = another_function(5, b=3)
        
        assert result == 15
        assert "Entering function: another_function" in caplog.text
        assert "Args: (5,), Kwargs: {'b': 3}" in caplog.text
        assert "Exiting function: another_function" in caplog.text
    
    def test_log_execution_exception(self, caplog):
        @log_execution()
        def error_function():
            raise ValueError("Test error")
        
        caplog.set_level(logging.ERROR)
        
        with pytest.raises(ValueError, match="Test error"):
            error_function()
        
        assert "Exception in error_function: Test error" in caplog.text