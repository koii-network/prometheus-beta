import logging
import pytest
from io import StringIO
import sys

from src.multi_log import log_multiple

def test_log_multiple_default():
    # Capture log output
    log_capture = StringIO()
    handler = logging.StreamHandler(log_capture)
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)

    # Log multiple values
    log_multiple('info', 'Hello', 123, 'World')
    
    # Check log output
    log_output = log_capture.getvalue().strip()
    assert 'Hello 123 World' in log_output

def test_log_multiple_different_levels():
    # Test different logging levels
    log_capture = StringIO()
    handler = logging.StreamHandler(log_capture)
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.DEBUG)

    # Test debug level
    log_multiple('debug', 'Debug', 'message')
    debug_output = log_capture.getvalue().strip()
    assert 'Debug message' in debug_output

    # Test error level
    log_capture.truncate(0)
    log_capture.seek(0)
    log_multiple('error', 'Error', 'occurred', 42)
    error_output = log_capture.getvalue().strip()
    assert 'Error occurred 42' in error_output

def test_log_multiple_custom_logger():
    # Create a custom logger
    custom_logger = logging.getLogger('custom_logger')
    log_capture = StringIO()
    handler = logging.StreamHandler(log_capture)
    custom_logger.addHandler(handler)
    custom_logger.setLevel(logging.INFO)

    # Log with custom logger
    log_multiple('info', 'Custom', 'Logger', 'Test', logger=custom_logger)
    
    # Check log output
    log_output = log_capture.getvalue().strip()
    assert 'Custom Logger Test' in log_output

def test_log_multiple_invalid_level():
    # Capture log output
    log_capture = StringIO()
    handler = logging.StreamHandler(log_capture)
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)

    # Log with invalid level (should default to info)
    log_multiple('INVALID_LEVEL', 'Fallback', 'to', 'info')
    
    # Check log output
    log_output = log_capture.getvalue().strip()
    assert 'Fallback to info' in log_output