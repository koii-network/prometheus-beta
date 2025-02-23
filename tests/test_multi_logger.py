import pytest
import logging
import io
import sys
from src.multi_logger import log_multiple

def test_log_multiple_basic():
    """Test basic logging functionality"""
    # Capture log output
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    logger = logging.getLogger('test_logger')
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    # Log multiple values
    log_multiple('info', 'Hello', 123, 'World', logger=logger)
    
    # Check log output
    log_output = log_capture.getvalue().strip()
    assert 'Hello 123 World' in log_output

def test_log_multiple_different_levels():
    """Test logging at different levels"""
    log_levels = ['debug', 'info', 'warning', 'error', 'critical']
    
    for level in log_levels:
        # Capture log output
        log_capture = io.StringIO()
        handler = logging.StreamHandler(log_capture)
        logger = logging.getLogger(f'test_{level}_logger')
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)

        # Log multiple values
        log_multiple(level, 'Test', 'message', 'at', level, logger=logger)
        
        # Check log output
        log_output = log_capture.getvalue().strip()
        assert 'Test message at ' + level in log_output

def test_log_multiple_invalid_level():
    """Test that invalid logging levels raise a ValueError"""
    with pytest.raises(ValueError, match="Invalid logging level"):
        log_multiple('invalid_level', 'Some', 'message')

def test_log_multiple_mixed_types():
    """Test logging with mixed data types"""
    # Capture log output
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    logger = logging.getLogger('mixed_types_logger')
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    # Log multiple values with mixed types
    log_multiple('info', 'Number:', 42, 'Float:', 3.14, 'Bool:', True, logger=logger)
    
    # Check log output
    log_output = log_capture.getvalue().strip()
    assert 'Number: 42 Float: 3.14 Bool: True' in log_output

def test_log_multiple_empty_args():
    """Test logging with no arguments after level"""
    # Capture log output
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    logger = logging.getLogger('empty_args_logger')
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    # Log with no additional arguments
    log_multiple('info', logger=logger)
    
    # Check log output
    log_output = log_capture.getvalue().strip()
    assert log_output == ''  # No message logged