import logging
import pytest
from src.parameter_logger import log_parameters

# Create a logger to capture log messages
class LogCapture:
    def __init__(self):
        self.records = []
    
    def info(self, message):
        self.records.append(message)

def test_log_parameters_basic():
    # Create a log capture
    log_capture = LogCapture()
    
    # Define a test function with the decorator
    @log_parameters(logger=log_capture)
    def sample_function(a, b, c=None):
        return a + b
    
    # Call the function
    result = sample_function(1, 2)
    
    # Check the log records
    assert len(log_capture.records) == 3
    assert "Calling function: sample_function" in log_capture.records[0]
    assert "Parameter 'a': 1" in log_capture.records[1]
    assert "Parameter 'b': 2" in log_capture.records[2]
    assert result == 3

def test_log_parameters_with_default():
    # Create a log capture
    log_capture = LogCapture()
    
    # Define a test function with default and keyword arguments
    @log_parameters(logger=log_capture)
    def sample_function(a, b=10, c="default"):
        return a + b
    
    # Call the function with partial arguments
    result = sample_function(5, c="custom")
    
    # Check the log records
    assert len(log_capture.records) == 3
    assert "Calling function: sample_function" in log_capture.records[0]
    assert "Parameter 'a': 5" in log_capture.records[1]
    assert "Parameter 'b': 10" in log_capture.records[2]
    assert result == 15

def test_log_parameters_complex_types():
    # Create a log capture
    log_capture = LogCapture()
    
    # Define a function with complex types
    @log_parameters(logger=log_capture)
    def sample_function(lst, dct, obj=None):
        return len(lst) + len(dct)
    
    # Call the function with complex types
    result = sample_function([1, 2, 3], {"a": 1, "b": 2})
    
    # Check the log records
    assert len(log_capture.records) == 3
    assert "Calling function: sample_function" in log_capture.records[0]
    assert "Parameter 'lst': [1, 2, 3]" in log_capture.records[1]
    assert "Parameter 'dct': {'a': 1, 'b': 2}" in log_capture.records[2]
    assert result == 5