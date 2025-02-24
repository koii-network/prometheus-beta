import logging
import pytest
from src.parameter_logger import log_parameters

# Create a custom logger for testing
test_logger = logging.getLogger('test_logger')
test_logger.setLevel(logging.INFO)

# Capture log messages
class LogCapture:
    def __init__(self, logger):
        self.log_messages = []
        self.handler = logging.Handler()
        self.handler.emit = lambda record: self.log_messages.append(record.getMessage())
        logger.addHandler(self.handler)
    
    def get_logs(self):
        return self.log_messages

@log_parameters(logger=test_logger)
def sample_function(a, b, c=10):
    return a + b + c

@log_parameters()
def sample_function_default_logger(x, y, z=20):
    return x * y + z

def test_log_parameters_with_custom_logger():
    # Setup log capture
    log_capture = LogCapture(test_logger)
    
    # Call the function
    result = sample_function(5, 7, c=3)
    
    # Check the result
    assert result == 15
    
    # Check log messages
    logs = log_capture.get_logs()
    assert "Calling function: sample_function" in logs
    assert "Parameter 'a': 5" in logs
    assert "Parameter 'b': 7" in logs
    assert "Parameter 'c': 3" in logs

def test_log_parameters_with_default_logger(caplog):
    # Set logging level to INFO
    caplog.set_level(logging.INFO)
    
    # Call the function
    result = sample_function_default_logger(2, 3)
    
    # Check the result
    assert result == 26
    
    # Check log messages
    log_records = [record.message for record in caplog.records]
    assert "Calling function: sample_function_default_logger" in log_records
    assert "Parameter 'x': 2" in log_records
    assert "Parameter 'y': 3" in log_records
    assert "Parameter 'z': 20" in log_records

def test_log_parameters_with_different_argument_types():
    # Setup log capture
    log_capture = LogCapture(test_logger)
    
    # Test with various argument types
    @log_parameters(logger=test_logger)
    def multi_type_function(a_list, a_dict, a_str="default"):
        return len(a_list) + len(a_dict) + len(a_str)
    
    result = multi_type_function([1,2,3], {"a": 1, "b": 2}, a_str="test")
    
    # Check the result
    assert result == 9
    
    # Check log messages
    logs = log_capture.get_logs()
    assert "Calling function: multi_type_function" in logs
    assert "Parameter 'a_list': [1, 2, 3]" in logs
    assert "Parameter 'a_dict': {'a': 1, 'b': 2}" in logs
    assert "Parameter 'a_str': 'test'" in logs