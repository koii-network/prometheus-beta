import logging
import pytest
from src.parameter_logger import log_parameters

# Configure a custom logger for testing
test_logger = logging.getLogger('test_logger')
test_handler = logging.handlers.MemoryHandler(capacity=10, flushLevel=logging.INFO)
test_logger.addHandler(test_handler)
test_logger.setLevel(logging.INFO)

class TestParameterLogger:
    def test_log_parameters_basic(self):
        # Reset the memory handler
        test_handler.flush()
        
        @log_parameters(logger=test_logger)
        def sample_function(a, b, c=10):
            return a + b + c
        
        # Call the function
        result = sample_function(1, 2, c=3)
        
        # Assert the function works correctly
        assert result == 6
        
        # Check logged messages
        log_records = test_handler.buffer
        assert len(log_records) >= 3  # Function name + parameters
        
        # Check function name is logged
        assert any('Calling function: sample_function' in record.getMessage() for record in log_records)
        
        # Check parameters are logged
        assert any("Parameter 'a': 1" in record.getMessage() for record in log_records)
        assert any("Parameter 'b': 2" in record.getMessage() for record in log_records)
        assert any("Parameter 'c': 3" in record.getMessage() for record in log_records)
    
    def test_log_parameters_default_values(self):
        # Reset the memory handler
        test_handler.flush()
        
        @log_parameters(logger=test_logger)
        def sample_function_with_defaults(x, y=5, z=None):
            return x + y
        
        # Call the function with some default arguments
        result = sample_function_with_defaults(10)
        
        # Assert the function works correctly
        assert result == 15
        
        # Check logged messages
        log_records = test_handler.buffer
        assert len(log_records) >= 3  # Function name + parameters
        
        # Check function name is logged
        assert any('Calling function: sample_function_with_defaults' in record.getMessage() for record in log_records)
        
        # Check parameters are logged with default values
        assert any("Parameter 'x': 10" in record.getMessage() for record in log_records)
        assert any("Parameter 'y': 5" in record.getMessage() for record in log_records)
        assert any("Parameter 'z': None" in record.getMessage() for record in log_records)
    
    def test_log_parameters_no_logger(self):
        # Test when no logger is provided (should use root logger)
        @log_parameters()
        def sample_function(a, b):
            return a + b
        
        # This should not raise an exception
        result = sample_function(1, 2)
        assert result == 3