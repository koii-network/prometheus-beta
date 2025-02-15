import logging
import pytest
import io
import sys
from src.error_logger import log_error

# Capture log output
def capture_logs(func):
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(logging.ERROR)
    
    try:
        func()
    finally:
        logging.getLogger().removeHandler(handler)
    
    return log_capture.getvalue()

def test_error_logging():
    @log_error
    def raise_error():
        raise ValueError("Test error")
    
    # Capture system error output
    with pytest.raises(ValueError):
        log_output = capture_logs(raise_error)
        
        # Check if log contains key information
        assert "Error in raise_error" in log_output
        assert "Test error" in log_output

def test_error_logging_details():
    @log_error
    def complex_error(x, y):
        return x / y
    
    # Test division by zero
    with pytest.raises(ZeroDivisionError):
        log_output = capture_logs(lambda: complex_error(10, 0))
        
        # Check if log contains key information
        assert "Error in complex_error" in log_output
        assert "division by zero" in log_output