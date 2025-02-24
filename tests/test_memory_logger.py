import pytest
import logging
import sys
import os
import io

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from memory_logger import log_memory_usage

def test_log_memory_usage():
    """Test that memory usage logging works and returns a non-empty dict"""
    # Capture log output
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    logger = logging.getLogger('test_logger')
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    # Call the function
    stats = log_memory_usage(logger)

    # Check return value
    assert isinstance(stats, dict), "Should return a dictionary"
    assert 'rss' in stats, "RSS memory should be in the stats"
    assert 'vms' in stats, "VMS memory should be in the stats"
    assert stats['rss'] > 0, "RSS memory should be a positive number"
    assert stats['vms'] > 0, "VMS memory should be a positive number"

    # Check log output
    log_output = log_capture.getvalue()
    assert "Memory Usage Statistics" in log_output
    assert "RSS:" in log_output
    assert "VMS:" in log_output

def test_log_memory_usage_default_logger():
    """Test logging with default logger"""
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Call the function without a logger
    stats = log_memory_usage()

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Check return value
    assert isinstance(stats, dict), "Should return a dictionary"
    assert 'rss' in stats, "RSS memory should be in the stats"
    assert 'vms' in stats, "VMS memory should be in the stats"

def test_log_memory_usage_optional_attributes():
    """Test that optional memory attributes are handled gracefully"""
    stats = log_memory_usage()

    # These might not always be available, so just check they exist
    assert 'uss' in stats
    assert 'pss' in stats