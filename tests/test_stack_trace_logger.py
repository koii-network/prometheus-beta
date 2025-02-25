import pytest
import logging
import sys
from src.stack_trace_logger import log_stack_trace

# Configure a test logger
class MockLogger:
    def __init__(self):
        self.logged_messages = []
    
    def log(self, level, message):
        self.logged_messages.append((level, message))

def test_log_stack_trace_with_current_exception():
    mock_logger = MockLogger()
    
    try:
        # Intentionally raise an exception
        raise ValueError("Test exception")
    except ValueError as e:
        # Log the stack trace
        trace = log_stack_trace(logger=mock_logger)
        
        # Assertions
        assert len(mock_logger.logged_messages) == 1
        assert mock_logger.logged_messages[0][0] == logging.ERROR
        assert "ValueError: Test exception" in mock_logger.logged_messages[0][1]
        assert "test_log_stack_trace_with_current_exception" in mock_logger.logged_messages[0][1]
        assert trace is not None

def test_log_stack_trace_with_provided_exception():
    mock_logger = MockLogger()
    
    # Create a test exception
    test_exception = ValueError("Provided exception")
    
    # Log the stack trace
    trace = log_stack_trace(exception=test_exception, logger=mock_logger)
    
    # Assertions
    assert len(mock_logger.logged_messages) == 1
    assert mock_logger.logged_messages[0][0] == logging.ERROR
    assert "ValueError: Provided exception" in mock_logger.logged_messages[0][1]
    assert trace is not None

def test_log_stack_trace_without_exception():
    mock_logger = MockLogger()
    
    # Test without an active exception
    trace = log_stack_trace(logger=mock_logger)
    
    # Assertions
    assert trace == "No active exception found."
    assert len(mock_logger.logged_messages) == 1
    assert mock_logger.logged_messages[0][0] == logging.ERROR
    assert "No active exception found." in mock_logger.logged_messages[0][1]

def test_log_stack_trace_custom_log_level():
    mock_logger = MockLogger()
    
    try:
        # Intentionally raise an exception
        raise RuntimeError("Custom level test")
    except RuntimeError as e:
        # Log the stack trace with a custom log level
        trace = log_stack_trace(exception=e, log_level=logging.WARNING, logger=mock_logger)
        
        # Assertions
        assert len(mock_logger.logged_messages) == 1
        assert mock_logger.logged_messages[0][0] == logging.WARNING
        assert "RuntimeError: Custom level test" in mock_logger.logged_messages[0][1]
        assert trace is not None