import logging
import pytest
from src.input_validation_logger import log_input_validation, validate_input

# Configure logging for test visibility
logging.basicConfig(level=logging.DEBUG)

def test_log_input_validation_decorator():
    # Create a custom logger to capture logs
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.DEBUG)
    
    # Create a log capture handler
    log_capture = []
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    # Sample function to decorate
    @log_input_validation(logger=logger)
    def sample_function(a, b, c=None):
        return a + b
    
    # Call the decorated function
    result = sample_function(1, 2, c=3)
    
    # Assert function works correctly
    assert result == 3

def test_validate_input_with_custom_validator():
    # Test input validation with a custom validator
    def is_positive(x):
        return x > 0
    
    # Successful validation
    result = validate_input(5, validator=is_positive)
    assert result == 5
    
    # Failed validation
    with pytest.raises(ValueError):
        validate_input(-1, validator=is_positive)

def test_validate_input_with_custom_error_message():
    # Test input validation with a custom error message
    def is_even(x):
        return x % 2 == 0
    
    # Successful validation
    result = validate_input(4, validator=is_even)
    assert result == 4
    
    # Failed validation with custom error message
    with pytest.raises(ValueError, match="Must be an even number"):
        validate_input(3, 
                       validator=is_even, 
                       error_message="Must be an even number")

def test_validate_input_without_validator():
    # Test validate_input without a validator
    result = validate_input("test")
    assert result == "test"

def test_log_input_validation_with_no_logger():
    # Test the log_input_validation decorator when no logger is provided
    @log_input_validation()
    def sample_function(x, y):
        return x + y
    
    # Ensure function still works correctly
    result = sample_function(1, 2)
    assert result == 3