import logging
import pytest
from src.input_validation_logger import log_input_validation

# Create a logger for testing
test_logger = logging.getLogger('test_logger')
test_handler = logging.Handler()
test_logger.addHandler(test_handler)
test_logger.setLevel(logging.DEBUG)

class TestInputValidationLogger:
    def test_successful_validation(self, caplog):
        @log_input_validation(logger=test_logger)
        def sample_func(x: int, y: int):
            return x + y
        
        caplog.set_level(logging.INFO)
        result = sample_func(5, 3)
        
        assert result == 8
        assert "Validating inputs for sample_func" in caplog.text
        assert "Input validation successful for sample_func" in caplog.text
    
    def test_value_error_validation(self):
        @log_input_validation(logger=test_logger)
        def validate_positive(x: int):
            if x <= 0:
                raise ValueError("Value must be positive")
            return x
        
        with pytest.raises(ValueError) as excinfo:
            validate_positive(-5)
        
        assert "Value must be positive" in str(excinfo.value)
    
    def test_type_error_validation(self):
        @log_input_validation(logger=test_logger)
        def validate_type(x: int):
            if not isinstance(x, int):
                raise TypeError("Input must be an integer")
            return x
        
        with pytest.raises(TypeError) as excinfo:
            validate_type("not an int")
        
        assert "Input must be an integer" in str(excinfo.value)
    
    def test_default_logger(self):
        @log_input_validation()
        def sample_func(x: int):
            return x
        
        # This should not raise any exceptions
        result = sample_func(10)
        assert result == 10