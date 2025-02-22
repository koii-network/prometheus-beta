import logging
import pytest
from src.input_validation_logger import log_input_validation

# Set up a capture handler for logging
class LogCapture:
    def __init__(self):
        self.log_records = []
        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(levelname)s: %(message)s')
        self.handler.setFormatter(self.formatter)
        
    def attach(self, logger):
        logger.addHandler(self.handler)
        logger.setLevel(logging.DEBUG)
        
    def detach(self, logger):
        logger.removeHandler(self.handler)

def test_log_input_validation_success():
    # Create a logger and log capture
    logger = logging.getLogger('test_logger')
    log_capture = LogCapture()
    log_capture.attach(logger)
    
    # Create a sample function with input validation
    @log_input_validation(logger)
    def sample_func(x: int, y: int):
        if x < 0 or y < 0:
            raise ValueError("Inputs must be non-negative")
        return x + y
    
    # Test successful validation
    result = sample_func(5, 3)
    assert result == 8
    
    # Check log messages
    log_records = log_capture.handler.stream.getvalue()
    assert "Validating inputs for sample_func" in log_records
    assert "Input validation successful for sample_func" in log_records
    
    log_capture.detach(logger)

def test_log_input_validation_value_error():
    # Create a logger and log capture
    logger = logging.getLogger('test_logger')
    log_capture = LogCapture()
    log_capture.attach(logger)
    
    # Create a sample function with input validation
    @log_input_validation(logger)
    def sample_func(x: int, y: int):
        if x < 0 or y < 0:
            raise ValueError("Inputs must be non-negative")
        return x + y
    
    # Test validation failure
    with pytest.raises(ValueError, match="Inputs must be non-negative"):
        sample_func(-1, 3)
    
    # Check log messages
    log_records = log_capture.handler.stream.getvalue()
    assert "Validating inputs for sample_func" in log_records
    assert "Input validation failed for sample_func" in log_records
    
    log_capture.detach(logger)

def test_log_input_validation_type_error():
    # Create a logger and log capture
    logger = logging.getLogger('test_logger')
    log_capture = LogCapture()
    log_capture.attach(logger)
    
    # Create a sample function with input validation
    @log_input_validation(logger)
    def sample_func(x: int, y: int):
        return x + y
    
    # Test type validation failure
    with pytest.raises(TypeError):
        sample_func("not", "integers")
    
    # Check log messages
    log_records = log_capture.handler.stream.getvalue()
    assert "Validating inputs for sample_func" in log_records
    assert "Input type validation failed for sample_func" in log_records
    
    log_capture.detach(logger)