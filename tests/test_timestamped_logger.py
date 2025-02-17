import os
import logging
import pytest
from src.timestamped_logger import log_with_timestamp

def test_log_with_timestamp_default():
    """Test logging with default parameters"""
    log_file = 'logs/app.log'
    if os.path.exists(log_file):
        os.remove(log_file)
    
    result = log_with_timestamp("Test default logging")
    assert result is True
    
    # Verify log file was created
    assert os.path.exists(log_file)

def test_log_with_timestamp_different_levels():
    """Test logging with different log levels"""
    levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    
    for level in levels:
        log_file = f'logs/app_{level.lower()}.log'
        if os.path.exists(log_file):
            os.remove(log_file)
        
        result = log_with_timestamp(f"Test {level} logging", log_level=level, log_file=f'app_{level.lower()}.log')
        assert result is True
        
        # Verify log file was created
        assert os.path.exists(log_file)

def test_log_with_timestamp_invalid_level():
    """Test that invalid log levels raise a ValueError"""
    with pytest.raises(ValueError, match="Invalid log level"):
        log_with_timestamp("Test invalid logging", log_level="INVALID")

def test_log_with_timestamp_log_contents():
    """Test that log contents are correct"""
    log_file = 'logs/test_contents.log'
    if os.path.exists(log_file):
        os.remove(log_file)
    
    test_message = "Logging test message"
    log_with_timestamp(test_message, log_level='INFO', log_file='test_contents.log')
    
    # Read log file and verify contents
    with open(os.path.join('logs', 'test_contents.log'), 'r') as f:
        log_contents = f.read()
        assert test_message in log_contents
        assert 'INFO' in log_contents