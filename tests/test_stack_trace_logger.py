import pytest
import logging
import sys
from src.stack_trace_logger import log_stack_trace

class MockLogger:
    def __init__(self):
        self.logged_messages = []
    
    def log(self, level, message):
        self.logged_messages.append((level, message))
    
    def error(self, message):
        self.logged_messages.append((logging.ERROR, message))

def test_log_stack_trace_with_exception():
    mock_logger = MockLogger()
    
    try:
        raise ValueError("Test exception")
    except ValueError as e:
        stack_trace = log_stack_trace(e, logger=mock_logger)
        
        assert len(mock_logger.logged_messages) == 1
        logged_level, logged_message = mock_logger.logged_messages[0]
        
        assert logged_level == logging.ERROR
        assert "ValueError: Test exception" in logged_message
        assert "test_log_stack_trace_with_exception" in logged_message
        assert stack_trace == logged_message

def test_log_stack_trace_current_exception():
    mock_logger = MockLogger()
    
    try:
        raise RuntimeError("Current exception")
    except RuntimeError:
        stack_trace = log_stack_trace(logger=mock_logger)
        
        assert len(mock_logger.logged_messages) == 1
        logged_level, logged_message = mock_logger.logged_messages[0]
        
        assert logged_level == logging.ERROR
        assert "RuntimeError: Current exception" in logged_message
        assert "test_log_stack_trace_current_exception" in logged_message
        assert stack_trace == logged_message

def test_log_stack_trace_no_exception():
    mock_logger = MockLogger()
    
    stack_trace = log_stack_trace(logger=mock_logger)
    
    assert stack_trace == ""
    assert len(mock_logger.logged_messages) == 0

def test_log_stack_trace_custom_log_level():
    mock_logger = MockLogger()
    
    try:
        raise TypeError("Custom log level test")
    except TypeError as e:
        stack_trace = log_stack_trace(e, logger=mock_logger, log_level=logging.WARNING)
        
        assert len(mock_logger.logged_messages) == 1
        logged_level, logged_message = mock_logger.logged_messages[0]
        
        assert logged_level == logging.WARNING
        assert "TypeError: Custom log level test" in logged_message