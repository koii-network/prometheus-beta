import os
import pytest
import logging
from src.keylogger import KeystrokeLogger
from pynput.keyboard import Key, KeyCode

def test_keylogger_initialization():
    """Test that the KeystrokeLogger initializes correctly."""
    logger = KeystrokeLogger()
    assert os.path.exists('logs')
    assert logger.log_file.endswith('keystrokes.log')

def test_keylogger_logging(tmp_path):
    """Test that keystrokes are being logged."""
    # Set a custom log file in a temporary directory
    custom_log_path = tmp_path / 'custom_keystrokes.log'
    logger = KeystrokeLogger(log_file=str(custom_log_path))
    
    # Mock a key press
    logger.on_press(KeyCode.from_char('a'))
    
    # Check if the log file contains the expected content
    with open(custom_log_path, 'r') as f:
        log_content = f.read()
        assert 'Pressed: a' in log_content

def test_special_key_logging(tmp_path):
    """Test logging of special keys."""
    custom_log_path = tmp_path / 'special_keys.log'
    logger = KeystrokeLogger(log_file=str(custom_log_path))
    
    # Mock a special key press
    logger.on_press(Key.shift)
    
    # Check if the log file contains the expected content
    with open(custom_log_path, 'r') as f:
        log_content = f.read()
        assert 'Special key pressed: Key.shift' in log_content

def test_start_stop_logging():
    """Test starting and stopping the logger."""
    logger = KeystrokeLogger()
    
    # Start logging
    listener = logger.start_logging()
    assert listener.running
    
    # Stop logging
    logger.stop_logging()
    assert not listener.running