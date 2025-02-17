import os
import pytest
import logging
from src.keylogger import KeystrokeLogger
from pynput.keyboard import Key, KeyCode

class TestKeystrokeLogger:
    @pytest.fixture
    def log_file(self, tmp_path):
        """Fixture to create a temporary log file."""
        return str(tmp_path / "test_keystrokes.log")

    def test_initialization(self, log_file):
        """Test logger initialization."""
        logger = KeystrokeLogger(log_file)
        assert logger.log_file == log_file
        assert os.path.exists(os.path.dirname(log_file))

    def test_log_file_path(self, log_file):
        """Test getting log file path."""
        logger = KeystrokeLogger(log_file)
        assert logger.get_log_file_path() == log_file

    def test_logging_character_key(self, log_file, caplog):
        """Test logging a character key."""
        logger = KeystrokeLogger(log_file)
        caplog.set_level(logging.INFO)
        
        # Simulate key press
        mock_key = KeyCode.from_char('a')
        logger.on_press(mock_key)
        
        # Check log contents
        assert 'Key pressed: a' in caplog.text

    def test_logging_special_key(self, log_file, caplog):
        """Test logging a special key."""
        logger = KeystrokeLogger(log_file)
        caplog.set_level(logging.INFO)
        
        # Simulate special key press
        mock_key = Key.shift
        logger.on_press(mock_key)
        
        # Check log contents
        assert 'Special key pressed: Key.shift' in caplog.text

    def test_start_and_stop_logging(self, log_file):
        """Test starting and stopping logging."""
        logger = KeystrokeLogger(log_file)
        
        # Test start logging
        assert logger.start_logging() is True
        assert logger.listener is not None
        
        # Test stop logging
        assert logger.stop_logging() is True
        assert logger.listener is not None  # listener is not None but stopped

    def test_multiple_logging_sessions(self, log_file):
        """Test starting multiple logging sessions."""
        logger = KeystrokeLogger(log_file)
        
        # First session
        assert logger.start_logging() is True
        logger.stop_logging()
        
        # Second session
        assert logger.start_logging() is True
        logger.stop_logging()