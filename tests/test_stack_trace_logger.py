import io
import logging
import pytest
import sys
from src.stack_trace_logger import log_stack_trace


def test_log_stack_trace_with_exception():
    """Test logging a specific exception."""
    try:
        raise ValueError("Test exception")
    except ValueError as e:
        stack_trace = log_stack_trace(e)
        assert "ValueError: Test exception" in stack_trace
        assert "test_log_stack_trace_with_exception" in stack_trace


def test_log_stack_trace_current_exception():
    """Test logging the current exception."""
    def raise_exception():
        raise RuntimeError("Current exception test")

    try:
        raise_exception()
    except RuntimeError:
        stack_trace = log_stack_trace()
        assert "RuntimeError: Current exception test" in stack_trace
        assert "raise_exception" in stack_trace


def test_log_stack_trace_with_custom_logger():
    """Test logging with a custom logger."""
    custom_logger = logging.getLogger("test_logger")
    custom_handler = logging.StreamHandler(io.StringIO())
    custom_logger.addHandler(custom_handler)
    custom_logger.setLevel(logging.ERROR)

    try:
        raise TypeError("Custom logger test")
    except TypeError as e:
        log_stack_trace(e, logger=custom_logger)
        log_output = custom_handler.stream.getvalue()
        assert "TypeError: Custom logger test" in log_output


def test_log_stack_trace_with_output_stream():
    """Test logging to a custom output stream."""
    output_stream = io.StringIO()
    
    try:
        raise AttributeError("Output stream test")
    except AttributeError as e:
        log_stack_trace(e, output_stream=output_stream)
        log_content = output_stream.getvalue()
        assert "AttributeError: Output stream test" in log_content


def test_log_stack_trace_no_exception():
    """Test that an exception is raised when no exception is available."""
    with pytest.raises(ValueError, match="No exception found to trace."):
        log_stack_trace()