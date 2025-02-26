import pytest
import logging
import io
import psutil
from src.memory_logger import log_memory_usage

def test_log_memory_usage():
    """
    Test that log_memory_usage returns correct memory statistics
    and logs the information correctly.
    """
    # Capture log output
    log_capture = io.StringIO()
    logger = logging.getLogger()
    handler = logging.StreamHandler(log_capture)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    # Call the function
    memory_stats = log_memory_usage(logger)

    # Verify the returned dictionary
    assert isinstance(memory_stats, dict), "Should return a dictionary"
    
    # Check dictionary keys
    expected_keys = ['total', 'available', 'used', 'percent']
    for key in expected_keys:
        assert key in memory_stats, f"Missing key: {key}"
    
    # Validate memory statistics
    assert memory_stats['total'] > 0, "Total memory should be positive"
    assert 0 <= memory_stats['percent'] <= 100, "Percent should be between 0 and 100"
    assert memory_stats['used'] <= memory_stats['total'], "Used memory cannot exceed total memory"

    # Check logging output
    log_output = log_capture.getvalue()
    assert "Memory Usage Statistics:" in log_output
    assert "Total Memory:" in log_output
    assert "Available Memory:" in log_output
    assert "Used Memory:" in log_output
    assert "Memory Usage:" in log_output

def test_log_memory_usage_default_logger():
    """
    Test log_memory_usage with default logger
    """
    # Call the function without a custom logger
    memory_stats = log_memory_usage()
    
    # Basic validation
    assert isinstance(memory_stats, dict)
    assert 'total' in memory_stats