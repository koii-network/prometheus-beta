import logging
import pytest
from src.input_validation_logger import log_input_validation

# Configure logging for tests
logging.basicConfig(level=logging.DEBUG)

def test_log_input_validation_success(caplog):
    @log_input_validation()
    def example_function(x: int, y: int):
        if x < 0 or y < 0:
            raise ValueError("Inputs must be non-negative")
        return x + y
    
    # Test successful validation
    caplog.set_level(logging.INFO)
    result = example_function(5, 3)
    assert result == 8
    
    # Check log messages
    assert "Validating inputs for example_function" in caplog.text
    assert "Input validation successful for example_function" in caplog.text

def test_log_input_validation_value_error():
    @log_input_validation()
    def example_function(x: int, y: int):
        if x < 0 or y < 0:
            raise ValueError("Inputs must be non-negative")
        return x + y
    
    # Test validation failure
    with pytest.raises(ValueError, match="Inputs must be non-negative"):
        example_function(-1, 5)

def test_log_input_validation_type_error():
    @log_input_validation()
    def example_function(x: int, y: int):
        return x + y
    
    # Test type validation failure
    with pytest.raises(TypeError):
        example_function("not", "int")

def test_log_input_validation_with_custom_logger(caplog):
    # Create a custom logger
    custom_logger = logging.getLogger('custom_logger')
    custom_logger.setLevel(logging.DEBUG)
    
    @log_input_validation(logger=custom_logger)
    def example_function(x: int, y: int):
        return x + y
    
    # Capture logs from custom logger
    result = example_function(5, 3)
    assert result == 8