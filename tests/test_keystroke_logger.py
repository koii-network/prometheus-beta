import os
import pytest
import logging
import tempfile
import pynput.keyboard
from src.keystroke_logger import KeystrokeLogger

class TestKeystrokeLogger:
    @pytest.fixture
    def logger(self):
        """Create a logger with a temporary log file."""
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.log') as temp_log:
            temp_log_path = temp_log.name
        
        logger = KeystrokeLogger(log_file=os.path.basename(temp_log_path))
        yield logger
        
        # Clean up: remove the temporary log file
        if os.path.exists(temp_log_path):
            os.unlink(temp_log_path)
    
    def test_logger_initialization(self, logger):
        """Test that the logger is initialized correctly."""
        assert os.path.exists(os.path.join('logs', os.path.basename(logger.log_file)))
        assert logger.listener is None
    
    def test_start_and_stop_logging(self, logger):
        """Test starting and stopping the logger."""
        logger.start()
        assert logger.listener is not None
        assert logger.listener.running
        
        logger.stop()
        assert not logger.listener.running
    
    def test_log_file_creation(self, logger):
        """Test that logging to a file works."""
        logger.start()
        
        # Simulate a key press
        key_event = pynput.keyboard.KeyCode.from_char('a')
        logger._on_press(key_event)
        
        logger.stop()
        
        # Check log file contents
        with open(os.path.join('logs', os.path.basename(logger.log_file)), 'r') as log_file:
            log_contents = log_file.read()
            assert "Key pressed: a" in log_contents
    
    def test_special_key_logging(self, logger):
        """Test logging of special keys."""
        logger.start()
        
        # Simulate a special key press
        key_event = pynput.keyboard.Key.enter
        logger._on_press(key_event)
        
        logger.stop()
        
        # Check log file contents
        with open(os.path.join('logs', os.path.basename(logger.log_file)), 'r') as log_file:
            log_contents = log_file.read()
            assert "Key pressed: Key.enter" in log_contents