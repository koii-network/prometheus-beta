import pytest
import logging
import io
import sys
from src.memory_logger import log_memory_usage

def test_log_memory_usage():
    # Capture log output
    log_capture = io.StringIO()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(log_capture)
    logger.addHandler(handler)

    # Call the function
    result = log_memory_usage(logger)

    # Remove the handler to prevent log duplication
    logger.removeHandler(handler)

    # Check the result is a dictionary with expected keys
    assert isinstance(result, dict)
    assert 'rss' in result
    assert 'vms' in result
    assert 'percent' in result

    # Check values are numeric and make sense
    assert result['rss'] >= 0
    assert result['vms'] >= 0
    assert 0 <= result['percent'] <= 100

    # Check logging output
    log_output = log_capture.getvalue()
    assert "Memory Usage Statistics:" in log_output
    assert "Resident Set Size (RSS):" in log_output
    assert "Virtual Memory Size (VMS):" in log_output
    assert "Total System Memory Usage:" in log_output

def test_log_memory_usage_default_logger():
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Call the function without a logger
    result = log_memory_usage()

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Basic checks
    assert isinstance(result, dict)
    assert 'rss' in result
    assert 'vms' in result
    assert 'percent' in result