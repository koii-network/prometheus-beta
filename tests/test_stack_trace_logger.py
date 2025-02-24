import logging
import pytest
import sys
from src.stack_trace_logger import log_stack_trace

class MockLogger:
    def __init__(self):
        self.logged_messages = []
        self.logged_levels = []

    def log(self, level, message):
        self.logged_messages.append(message)
        self.logged_levels.append(level)

def test_log_stack_trace_current_exception():
    mock_logger = MockLogger()
    
    try:
        raise ValueError("Test exception")
    except ValueError as e:
        stack_trace = log_stack_trace(logger=mock_logger)
        
        assert len(mock_logger.logged_messages) == 1
        assert mock_logger.logged_levels[0] == logging.ERROR
        assert "test_log_stack_trace_current_exception" in stack_trace
        assert "ValueError: Test exception" in stack_trace

def test_log_stack_trace_provided_exception():
    mock_logger = MockLogger()
    
    try:
        raise RuntimeError("Specific error")
    except RuntimeError as original_exception:
        stack_trace = log_stack_trace(
            exception=original_exception, 
            logger=mock_logger, 
            log_level=logging.CRITICAL
        )
        
        assert len(mock_logger.logged_messages) == 1
        assert mock_logger.logged_levels[0] == logging.CRITICAL
        assert "RuntimeError: Specific error" in stack_trace

def test_log_stack_trace_no_exception():
    mock_logger = MockLogger()
    
    stack_trace = log_stack_trace(logger=mock_logger)
    
    assert stack_trace == "No active exception found."
    assert len(mock_logger.logged_messages) == 1

def test_log_stack_trace_invalid_logger():
    with pytest.raises(TypeError):
        log_stack_trace(logger="not a logger")

def test_log_stack_trace_different_log_levels():
    mock_logger = MockLogger()
    
    try:
        raise TypeError("Level test")
    except TypeError as e:
        stack_trace = log_stack_trace(
            exception=e, 
            logger=mock_logger, 
            log_level=logging.WARNING
        )
        
        assert mock_logger.logged_levels[0] == logging.WARNING
        assert "TypeError: Level test" in stack_trace