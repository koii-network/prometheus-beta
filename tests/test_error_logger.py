import pytest
import logging
import io
import sys
from src.error_logger import log_error

# Capture log output
class LogCapture:
    def __init__(self):
        self.captured = io.StringIO()
        self.handler = logging.StreamHandler(self.captured)
        logging.getLogger().addHandler(self.handler)
        logging.getLogger().setLevel(logging.ERROR)

    def get_log_contents(self):
        self.handler.flush()
        return self.captured.getvalue()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        logging.getLogger().removeHandler(self.handler)
        self.captured.close()

# Test functions
@log_error()
def raise_generic_error():
    raise ValueError("Test error")

@log_error("Custom error message")
def raise_error_with_custom_message():
    raise RuntimeError("Specific runtime error")

def test_default_error_logging():
    with LogCapture() as log_capture:
        with pytest.raises(ValueError):
            raise_generic_error()
        
        log_output = log_capture.get_log_contents()
        assert "An error occurred" in log_output
        assert "Test error" in log_output

def test_custom_error_message():
    with LogCapture() as log_capture:
        with pytest.raises(RuntimeError):
            raise_error_with_custom_message()
        
        log_output = log_capture.get_log_contents()
        assert "Custom error message" in log_output
        assert "Specific runtime error" in log_output

def test_exception_reraising():
    # Ensure the original exception is re-raised
    with pytest.raises(ValueError):
        raise_generic_error()

    with pytest.raises(RuntimeError):
        raise_error_with_custom_message()