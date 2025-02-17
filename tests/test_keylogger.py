import os
import logging
import pytest
from unittest.mock import MagicMock, patch
from src.keylogger import KeystrokeLogger
import pynput

def test_keylogger_initialization():
    """
    Test that the KeystrokeLogger initializes correctly
    """
    log_file = 'test_keystrokes.log'
    keylogger = KeystrokeLogger(log_file)
    
    # Check that the logger is created
    assert keylogger.logger is not None
    
    # Cleanup log file after test
    if os.path.exists(log_file):
        os.remove(log_file)

def test_on_press_method():
    """
    Test the on_press method logging functionality
    """
    log_file = 'test_keypress.log'
    keylogger = KeystrokeLogger(log_file)
    
    # Create a mock key
    mock_key = MagicMock()
    mock_key.char = 'a'
    
    # Patch logging to capture log message
    with patch.object(keylogger.logger, 'info') as mock_log:
        keylogger.on_press(mock_key)
        mock_log.assert_called_once_with('Key pressed: a')
    
    # Cleanup log file after test
    if os.path.exists(log_file):
        os.remove(log_file)

def test_start_and_stop_logging():
    """
    Test starting and stopping the keylogger
    """
    keylogger = KeystrokeLogger()
    
    # Patch the keyboard listener
    with patch('pynput.keyboard.Listener') as MockListener:
        mock_listener = MagicMock()
        MockListener.return_value = mock_listener
        
        # Start logging
        listener = keylogger.start_logging()
        mock_listener.start.assert_called_once()
        
        # Stop logging
        keylogger.stop_logging()
        mock_listener.stop.assert_called_once()

def test_special_key_logging():
    """
    Test logging of special keys
    """
    log_file = 'test_special_key.log'
    keylogger = KeystrokeLogger(log_file)
    
    # Create a mock special key
    mock_key = MagicMock()
    del mock_key.char  # Remove char to simulate special key
    mock_key.__str__.return_value = 'Key.shift'
    
    # Patch logging to capture log message
    with patch.object(keylogger.logger, 'info') as mock_log:
        keylogger.on_press(mock_key)
        mock_log.assert_called_once_with('Special key pressed: Key.shift')
    
    # Cleanup log file after test
    if os.path.exists(log_file):
        os.remove(log_file)