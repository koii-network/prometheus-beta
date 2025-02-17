import logging
import pytest
from src.input_validation_logger import log_input_validation

# Configure logging for test
logging.basicConfig(level=logging.DEBUG)

class TestInputValidationLogger:
    def test_successful_validation(self, caplog):
        @log_input_validation()
        def example_func(x: int, y: int):
            if x < 0 or y < 0:
                raise ValueError("Inputs must be non-negative")
            return x + y
        
        caplog.set_level(logging.INFO)
        result = example_func(5, 3)
        assert result == 8
        
        # Check log messages
        assert "Validating inputs for example_func" in caplog.text
        assert "Input validation successful for example_func" in caplog.text
    
    def test_failed_validation_value_error(self, caplog):
        @log_input_validation()
        def example_func(x: int, y: int):
            if x < 0 or y < 0:
                raise ValueError("Inputs must be non-negative")
            return x + y
        
        caplog.set_level(logging.ERROR)
        with pytest.raises(ValueError, match="Inputs must be non-negative"):
            example_func(-1, 3)
        
        # Check error log message
        assert "Input validation failed for example_func" in caplog.text
    
    def test_failed_validation_type_error(self, caplog):
        @log_input_validation()
        def example_func(x: int, y: int):
            return x + y
        
        caplog.set_level(logging.ERROR)
        with pytest.raises(TypeError):
            example_func("not", "int")
        
        # Check error log message
        assert "Input type validation failed for example_func" in caplog.text
    
    def test_custom_logger(self, caplog):
        # Create a custom logger
        custom_logger = logging.getLogger('custom_logger')
        custom_logger.setLevel(logging.DEBUG)
        
        @log_input_validation(logger=custom_logger)
        def example_func(x: int, y: int):
            return x + y
        
        result = example_func(5, 3)
        assert result == 8
        
        # Verify custom logger usage
        # Note: This might require more complex logging capture
        assert "Validating inputs for example_func" in caplog.text