import logging
import pytest
from src.debug_logger import conditional_debug_log

# Create a custom logger for testing
test_logger = logging.getLogger('test_logger')
test_logger.setLevel(logging.DEBUG)

# Capture logs for testing
class LogCapture:
    def __init__(self, logger):
        self.logger = logger
        self.handler = logging.StreamHandler()
        self.formatter = logging.Formatter('%(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
        self.log_messages = []
        self.handler.stream.seek(0)
        self.old_handlers = self.logger.handlers[:]

    def get_log_messages(self):
        self.handler.flush()
        return self.log_messages

    def __enter__(self):
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.handler.close()
        self.logger.handlers = self.old_handlers

def test_conditional_debug_log_enabled():
    """Test that debug logs are produced when condition is True."""
    @conditional_debug_log(condition=True, logger=test_logger)
    def sample_function(x, y):
        return x + y

    with LogCapture(test_logger) as log_capture:
        result = sample_function(3, 4)
        
    # Check function works correctly
    assert result == 7
    
    # Check log messages
    log_messages = log_capture.get_log_messages()
    assert any("Entering function: sample_function" in msg for msg in log_messages)
    assert any("Arguments: args=(3, 4), kwargs={}" in msg for msg in log_messages)
    assert any("Exiting function: sample_function" in msg for msg in log_messages)
    assert any("Return value: 7" in msg for msg in log_messages)

def test_conditional_debug_log_disabled():
    """Test that debug logs are not produced when condition is False."""
    @conditional_debug_log(condition=False, logger=test_logger)
    def sample_function(x, y):
        return x + y

    with LogCapture(test_logger) as log_capture:
        result = sample_function(3, 4)
        
    # Check function works correctly
    assert result == 7
    
    # Check no log messages were produced
    log_messages = log_capture.get_log_messages()
    assert len(log_messages) == 0

def test_conditional_debug_log_default_logger():
    """Test that the default logger works when no logger is specified."""
    @conditional_debug_log(condition=True)
    def sample_function(x, y):
        return x + y

    # Simply ensure no exceptions are raised
    result = sample_function(3, 4)
    assert result == 7

def test_conditional_debug_log_with_kwargs():
    """Test debug logging with keyword arguments."""
    @conditional_debug_log(condition=True, logger=test_logger)
    def sample_function(x, y, z=0):
        return x + y + z

    with LogCapture(test_logger) as log_capture:
        result = sample_function(3, 4, z=5)
        
    # Check function works correctly
    assert result == 12
    
    # Check log messages
    log_messages = log_capture.get_log_messages()
    assert any("Entering function: sample_function" in msg for msg in log_messages)
    assert any("Arguments: args=(3, 4), kwargs={'z': 5}" in msg for msg in log_messages)
    assert any("Exiting function: sample_function" in msg for msg in log_messages)
    assert any("Return value: 12" in msg for msg in log_messages)