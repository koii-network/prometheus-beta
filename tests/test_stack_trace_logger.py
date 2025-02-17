import logging
import pytest
import sys
from src.stack_trace_logger import log_stack_trace

class TestStackTraceLogger:
    def test_log_with_provided_exception(self):
        # Create a test logger
        logger = logging.getLogger('test_logger')
        logger.setLevel(logging.ERROR)
        
        # Create a test exception
        test_exception = ValueError("Test exception")
        
        # Log the stack trace
        trace = log_stack_trace(exception=test_exception, logger=logger)
        
        # Verify trace contains exception details
        assert "ValueError: Test exception" in trace
    
    def test_log_current_exception(self):
        # Create a test logger
        logger = logging.getLogger('test_logger')
        logger.setLevel(logging.ERROR)
        
        # Simulate an exception
        try:
            raise RuntimeError("Current exception test")
        except RuntimeError as e:
            trace = log_stack_trace(logger=logger)
            
            # Verify trace contains exception details
            assert "RuntimeError: Current exception test" in trace
    
    def test_log_no_exception(self):
        # Create a test logger
        logger = logging.getLogger('test_logger')
        logger.setLevel(logging.ERROR)
        
        # Call log_stack_trace with no exception outside of exception context
        trace = log_stack_trace(logger=logger)
        
        # Verify an empty string is returned
        assert trace == ""
    
    def test_different_log_levels(self):
        # Create a test logger
        logger = logging.getLogger('test_logger')
        logger.setLevel(logging.DEBUG)
        
        # Test different log levels
        test_exception = ValueError("Level test")
        
        # Log with different log levels
        for level in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]:
            trace = log_stack_trace(exception=test_exception, log_level=level, logger=logger)
            assert "ValueError: Level test" in trace