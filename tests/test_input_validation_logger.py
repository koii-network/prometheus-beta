import logging
import pytest
from src.input_validation_logger import log_input_validation

# Configure logging for tests
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TestInputValidationLogger:
    def test_successful_validation(self, caplog):
        @log_input_validation(logger)
        def sample_function(x: int, y: int):
            return x + y
        
        caplog.set_level(logging.INFO)
        result = sample_function(5, 3)
        
        assert result == 8
        assert "Validating inputs for sample_function" in caplog.text
        assert "Input validation successful" in caplog.text
    
    def test_validation_with_value_error(self, caplog):
        @log_input_validation(logger)
        def sample_function(x: int):
            if x < 0:
                raise ValueError("Value must be non-negative")
            return x
        
        caplog.set_level(logging.ERROR)
        
        with pytest.raises(ValueError, match="Value must be non-negative"):
            sample_function(-5)
        
        assert "Input validation failed" in caplog.text
    
    def test_validation_with_type_error(self, caplog):
        @log_input_validation(logger)
        def sample_function(x: str):
            if not isinstance(x, str):
                raise TypeError("Input must be a string")
            return x.upper()
        
        caplog.set_level(logging.ERROR)
        
        with pytest.raises(TypeError, match="Input must be a string"):
            sample_function(123)
        
        assert "Input type validation failed" in caplog.text
    
    def test_default_logger(self):
        @log_input_validation()
        def sample_function(x):
            return x
        
        # This test just ensures no exception is raised with default logger
        result = sample_function(10)
        assert result == 10