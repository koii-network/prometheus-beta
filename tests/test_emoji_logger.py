import logging
import pytest
import io
import sys
from src.emoji_logger import EmojiLogger, get_emoji_logger

class TestEmojiLogger:
    def setup_method(self):
        # Capture stdout for testing log output
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def teardown_method(self):
        # Restore stdout
        sys.stdout = sys.__stdout__

    def test_logger_creation(self):
        logger = EmojiLogger()
        assert logger is not None
        assert isinstance(logger, EmojiLogger)

    def test_log_info_without_emoji(self):
        logger = EmojiLogger()
        logger.log("Test message")
        output = self.captured_output.getvalue()
        assert "Test message" in output
        assert "INFO" in output

    def test_log_with_emoji(self):
        logger = EmojiLogger()
        logger.log("Test message", emoji_symbol=":smile:")
        output = self.captured_output.getvalue()
        assert "😄 Test message" in output

    def test_different_log_levels(self):
        logger = EmojiLogger()
        
        # Test debug
        logger.log("Debug message", level=logging.DEBUG, emoji_symbol=":bug:")
        # Test info
        logger.log("Info message", level=logging.INFO, emoji_symbol=":info:")
        # Test warning
        logger.log("Warning message", level=logging.WARNING, emoji_symbol=":warning:")
        # Test error
        logger.log("Error message", level=logging.ERROR, emoji_symbol=":x:")
        # Test critical
        logger.log("Critical message", level=logging.CRITICAL, emoji_symbol=":fire:")

        output = self.captured_output.getvalue()
        assert all(level in output for level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])

    def test_get_emoji_logger(self):
        logger = get_emoji_logger()
        assert isinstance(logger, EmojiLogger)

    def test_invalid_emoji(self):
        logger = EmojiLogger()
        # Should not raise an exception
        logger.log("Message", emoji_symbol="invalid_emoji")
        output = self.captured_output.getvalue()
        assert "Message" in output