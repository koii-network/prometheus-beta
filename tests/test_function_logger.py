import logging
import pytest
import time
from src.function_logger import log_execution

# Configure a test logger
test_logger = logging.getLogger('test_logger')
test_handler = logging.Handler()
test_logger.addHandler(test_handler)
test_logger.setLevel(logging.INFO)

class TestFunctionLogger:
    def test_basic_logging(self, caplog):
        """Test basic function logging"""
        @log_execution(logger=test_logger)
        def sample_function(x, y):
            return x + y
        
        caplog.set_level(logging.INFO)
        result = sample_function(3, 4)
        
        assert result == 7
        assert "Executing function: sample_function" in caplog.text
        assert "Arguments: args=(3, 4), kwargs={}" in caplog.text
        assert "Function sample_function completed successfully" in caplog.text
    
    def test_function_with_kwargs(self, caplog):
        """Test logging with keyword arguments"""
        @log_execution(logger=test_logger)
        def sample_function(x, y=0):
            return x + y
        
        caplog.set_level(logging.INFO)
        result = sample_function(3, y=5)
        
        assert result == 8
        assert "Arguments: args=(3,), kwargs={'y': 5}" in caplog.text
    
    def test_execution_time_logging(self, caplog):
        """Test that execution time is logged"""
        @log_execution(logger=test_logger)
        def slow_function():
            time.sleep(0.1)
        
        caplog.set_level(logging.INFO)
        slow_function()
        
        execution_log = [record for record in caplog.records 
                          if "Execution time:" in record.message]
        assert len(execution_log) == 1
        assert float(execution_log[0].message.split(':')[1].strip().split()[0]) >= 0.1
    
    def test_exception_logging(self, caplog):
        """Test logging of exceptions"""
        @log_execution(logger=test_logger)
        def error_function():
            raise ValueError("Test error")
        
        caplog.set_level(logging.ERROR)
        
        with pytest.raises(ValueError, match="Test error"):
            error_function()
        
        assert "Exception in function error_function" in caplog.text