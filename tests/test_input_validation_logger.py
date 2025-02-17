import pytest
import logging
from src.input_validation_logger import log_input_validation

# Capture log messages for testing
class LogCapture:
    def __init__(self):
        self.log_messages = []
    
    def info(self, message):
        self.log_messages.append(('INFO', message))
    
    def error(self, message):
        self.log_messages.append(('ERROR', message))

def test_log_input_validation_decorator():
    # Create a custom logger
    log_capture = LogCapture()
    
    # Test function with decorator
    @log_input_validation(logger=log_capture)
    def example_function(x: int, y: str = "default"):
        return x + len(y)
    
    # Call the function
    result = example_function(5, "test")
    
    # Check the result
    assert result == 9
    
    # Check log messages
    assert len(log_capture.log_messages) >= 3  # Typically includes start, parameter logs, and success
    assert ('INFO', "Validating inputs for function: example_function") in log_capture.log_messages
    assert ('INFO', "Parameter 'x': 5") in log_capture.log_messages
    assert ('INFO', "Parameter 'y': test") in log_capture.log_messages
    assert ('INFO', "Input validation successful for function: example_function") in log_capture.log_messages

def test_log_input_validation_type_error():
    # Create a custom logger
    log_capture = LogCapture()
    
    # Test function with decorator that will raise a TypeError
    @log_input_validation(logger=log_capture)
    def type_check_function(x: int):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        return x
    
    # Attempt to call with wrong type
    with pytest.raises(TypeError):
        type_check_function("not an int")
    
    # Check log messages include error
    assert any(
        message_type == 'ERROR' and 
        "Type validation error in type_check_function" in message 
        for message_type, message in log_capture.log_messages
    )

def test_log_input_validation_value_error():
    # Create a custom logger
    log_capture = LogCapture()
    
    # Test function with decorator that will raise a ValueError
    @log_input_validation(logger=log_capture)
    def value_check_function(x: int):
        if x < 0:
            raise ValueError("x must be non-negative")
        return x
    
    # Attempt to call with invalid value
    with pytest.raises(ValueError):
        value_check_function(-5)
    
    # Check log messages include error
    assert any(
        message_type == 'ERROR' and 
        "Value validation error in value_check_function" in message 
        for message_type, message in log_capture.log_messages
    )