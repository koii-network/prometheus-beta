import pytest
import logging
import io
from src.memory_logger import log_memory_usage

def test_log_memory_usage():
    # Capture log output
    log_capture = io.StringIO()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(log_capture)
    logger.addHandler(handler)
    
    # Call the function
    stats = log_memory_usage(logger)
    
    # Assertions
    assert isinstance(stats, dict), "Function should return a dictionary"
    
    # Check dictionary keys
    expected_keys = ['total', 'available', 'used', 'percent']
    for key in expected_keys:
        assert key in stats, f"Missing key: {key}"
    
    # Validate numeric values
    assert stats['total'] > 0, "Total memory should be greater than 0"
    assert stats['available'] >= 0, "Available memory should be non-negative"
    assert stats['used'] > 0, "Used memory should be greater than 0"
    assert 0 <= stats['percent'] <= 100, "Memory percentage should be between 0 and 100"
    
    # Check log output
    log_output = log_capture.getvalue()
    assert "Memory Usage Statistics" in log_output
    assert "Total Memory" in log_output
    assert "Available Memory" in log_output
    assert "Used Memory" in log_output
    assert "Memory Usage Percentage" in log_output

def test_log_memory_usage_default_logger():
    # Test with default logger
    stats = log_memory_usage()
    
    # Basic assertions
    assert isinstance(stats, dict), "Function should return a dictionary"
    assert 0 < stats['total'], "Total memory should be positive"
    assert 0 <= stats['percent'] <= 100, "Memory percentage should be between 0 and 100"