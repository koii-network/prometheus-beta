import logging
import pytest
from src.input_validation_logger import log_input_validation

# Configure logging for tests
logging.basicConfig(level=logging.DEBUG)

class TestInputValidationLogger:
    def test_successful_validation(self, caplog):
        @log_input_validation()
        def example_func(x: int, y: int):
            return x + y
        
        caplog.set_level(logging.INFO)
        result = example_func(5, 3)
        
        assert result == 8
        assert "Validating inputs for function: example_func" in caplog.text
        assert "Input validation successful" in caplog.text
    
    def test_failed_validation_type(self, caplog):
        @log_input_validation()
        def example_func(x: int, y: int):
            return x + y
        
        caplog.set_level(logging.ERROR)
        
        with pytest.raises(TypeError):
            example_func("not", "int")
        
        assert "Invalid input type" in caplog.text
    
    def test_failed_validation_value(self, caplog):
        @log_input_validation()
        def example_func(x: int):
            if x < 0:
                raise ValueError("Value must be non-negative")
            return x
        
        caplog.set_level(logging.ERROR)
        
        with pytest.raises(ValueError):
            example_func(-5)
        
        assert "Input validation failed" in caplog.text
    
    def test_custom_logger(self):
        custom_logger = logging.getLogger('custom_logger')
        custom_logger.setLevel(logging.DEBUG)
        
        @log_input_validation(logger=custom_logger)
        def example_func(x: int):
            return x
        
        example_func(10)  # This should use the custom logger