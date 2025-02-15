import pytest
import logging
import io
import sys
from src.memory_logger import log_memory_usage

def test_log_memory_usage():
    """
    Test the log_memory_usage function
    """
    # Capture logger output
    log_capture = io.StringIO()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(log_capture)
    logger.addHandler(handler)

    # Call the function
    memory_stats = log_memory_usage(logger)

    # Verify memory stats dictionary keys
    expected_keys = [
        'total_memory_bytes', 
        'available_memory_bytes', 
        'used_memory_bytes', 
        'memory_percent_used', 
        'process_memory_bytes'
    ]
    for key in expected_keys:
        assert key in memory_stats, f"Missing key: {key}"

    # Verify numeric values
    assert memory_stats['total_memory_bytes'] > 0, "Total memory should be positive"
    assert 0 <= memory_stats['memory_percent_used'] <= 100, "Memory percent should be between 0 and 100"
    assert memory_stats['process_memory_bytes'] > 0, "Process memory should be positive"

    # Verify logging
    log_output = log_capture.getvalue()
    assert "Memory Usage Statistics:" in log_output
    assert "Total Memory:" in log_output
    assert "Available Memory:" in log_output
    assert "Used Memory:" in log_output
    assert "Memory Usage Percentage:" in log_output
    assert "Current Process Memory:" in log_output

def test_log_memory_usage_default_logger():
    """
    Test log_memory_usage with default logger
    """
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()

    # Call function without providing a logger
    memory_stats = log_memory_usage()

    # Restore stdout
    sys.stdout = old_stdout

    # Verify results are similar to previous test
    assert isinstance(memory_stats, dict)
    assert len(memory_stats) == 5