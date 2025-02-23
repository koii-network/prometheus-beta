import pytest
import logging
import io
import sys
from src.memory_logger import log_memory_usage

def test_log_memory_usage():
    """
    Test the log_memory_usage function
    """
    # Capture log output
    log_capture = io.StringIO()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(log_capture)
    logger.addHandler(handler)

    # Call the function
    result = log_memory_usage(logger)

    # Assertions
    assert result is not None, "Memory stats should be returned"
    
    # Check dictionary keys
    expected_keys = ['total', 'available', 'used', 'percent']
    for key in expected_keys:
        assert key in result, f"Key {key} should be in memory stats"

    # Check value types
    assert isinstance(result['total'], float), "Total memory should be a float"
    assert isinstance(result['available'], float), "Available memory should be a float"
    assert isinstance(result['used'], float), "Used memory should be a float"
    assert isinstance(result['percent'], float), "Memory percentage should be a float"

    # Check log output
    log_output = log_capture.getvalue()
    assert "Memory Usage Statistics:" in log_output
    assert "Total Memory:" in log_output
    assert "Available Memory:" in log_output
    assert "Used Memory:" in log_output
    assert "Memory Usage Percentage:" in log_output

def test_log_memory_usage_default_logger():
    """
    Test log_memory_usage with default logger
    """
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()

    # Call the function without a logger
    result = log_memory_usage()

    # Restore stdout
    sys.stdout = old_stdout

    # Assertions
    assert result is not None, "Memory stats should be returned with default logger"

def test_memory_stats_validity():
    """
    Verify the validity of memory statistics
    """
    result = log_memory_usage()

    # Check percentage is between 0 and 100
    assert 0 <= result['percent'] <= 100, "Memory percentage should be between 0 and 100"

    # Check that used memory is less than or equal to total memory
    assert result['used'] <= result['total'], "Used memory cannot be greater than total memory"

    # Check that available memory makes sense
    assert result['available'] > 0, "Available memory should be positive"