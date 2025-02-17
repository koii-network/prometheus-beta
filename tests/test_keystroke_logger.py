import os
import logging
import pytest
from src.keystroke_logger import KeystrokeLogger
import tempfile

def test_keystroke_logger_initialization():
    """Test logger initialization creates log file in logs directory."""
    logger = KeystrokeLogger()
    assert os.path.exists('logs')
    assert logger.get_log_file_path().startswith('logs/')

def test_log_file_path():
    """Test that log file path is set correctly."""
    custom_log_file = 'custom_keystrokes.log'
    logger = KeystrokeLogger(log_file=custom_log_file)
    assert logger.get_log_file_path() == os.path.join('logs', custom_log_file)

def test_logging_configuration():
    """Test that logging is configured correctly."""
    logger = KeystrokeLogger()
    
    # Verify logging configuration
    root_logger = logging.getLogger()
    assert root_logger.level == logging.INFO
    
    # Check handlers
    handlers = root_logger.handlers
    assert len(handlers) > 0
    log_handler = handlers[0]
    assert isinstance(log_handler, logging.FileHandler)
    assert log_handler.baseFilename == os.path.abspath(logger.get_log_file_path())

def test_start_and_stop_logging():
    """Test starting and stopping the logging process."""
    logger = KeystrokeLogger()
    
    # Start logging
    listener = logger.start_logging()
    assert listener is not None
    assert listener.running
    
    # Stop logging
    logger.stop_logging()
    assert not listener.running

def test_multiple_start_calls():
    """Ensure multiple start calls don't create multiple listeners."""
    logger = KeystrokeLogger()
    
    first_listener = logger.start_logging()
    second_listener = logger.start_logging()
    
    assert first_listener == second_listener