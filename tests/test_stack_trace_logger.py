import pytest
import logging
import sys
from src.stack_trace_logger import log_stack_trace

def test_log_stack_trace_with_exception():
    """Test logging a specific exception"""
    try:
        raise ValueError("Test exception")
    except ValueError as e:
        trace = log_stack_trace(e)
        assert "ValueError" in trace
        assert "Test exception" in trace

def test_log_stack_trace_without_exception():
    """Test logging the current exception"""
    try:
        # Intentionally raise an exception
        1 / 0  
    except ZeroDivisionError:
        trace = log_stack_trace()
        assert "ZeroDivisionError" in trace
        assert "division by zero" in trace

def test_log_stack_trace_no_exception():
    """Test behavior when no exception exists"""
    # Temporarily suppress stderr to prevent printing
    import io
    import sys
    old_stderr = sys.stderr
    sys.stderr = io.StringIO()
    
    try:
        trace = log_stack_trace()
        assert trace == "No exception found to log."
    finally:
        # Restore stderr
        sys.stderr = old_stderr

def test_log_stack_trace_custom_log_level():
    """Test logging with a custom log level"""
    try:
        raise RuntimeError("Custom level test")
    except RuntimeError as e:
        trace = log_stack_trace(e, log_level=logging.CRITICAL)
        assert "RuntimeError" in trace
        assert "Custom level test" in trace