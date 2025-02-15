import logging
import pytest
from src.stack_trace_logger import log_stack_trace

# Create a custom logger for testing
class MockLogger:
    def __init__(self):
        self.logs = []
    
    def log(self, level, message):
        self.logs.append((level, message))

def test_log_stack_trace_with_no_exception():
    # Test logging current stack trace
    mock_logger = MockLogger()
    trace = log_stack_trace(logger=mock_logger)
    
    assert len(mock_logger.logs) == 1
    assert mock_logger.logs[0][0] == logging.ERROR
    assert "test_log_stack_trace_with_no_exception" in trace

def test_log_stack_trace_with_exception():
    # Test logging an exception's stack trace
    mock_logger = MockLogger()
    
    try:
        raise ValueError("Test exception")
    except ValueError as e:
        trace = log_stack_trace(exception=e, logger=mock_logger)
    
    assert len(mock_logger.logs) == 1
    assert mock_logger.logs[0][0] == logging.ERROR
    assert "ValueError: Test exception" in trace
    assert "test_log_stack_trace_with_exception" in trace

def test_log_stack_trace_custom_log_level():
    # Test custom log level
    mock_logger = MockLogger()
    
    trace = log_stack_trace(logger=mock_logger, log_level=logging.WARNING)
    
    assert len(mock_logger.logs) == 1
    assert mock_logger.logs[0][0] == logging.WARNING

def test_log_stack_trace_returns_string():
    # Ensure the function returns a string
    mock_logger = MockLogger()
    trace = log_stack_trace(logger=mock_logger)
    
    assert isinstance(trace, str)
    assert len(trace) > 0