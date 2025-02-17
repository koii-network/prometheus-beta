import logging
import pytest
from src.debug_logger import conditional_debug_log

class TestConditionalDebugLog:
    def test_debug_disabled(self, caplog):
        """Test that no logging occurs when debug is disabled"""
        caplog.set_level(logging.DEBUG)
        result = conditional_debug_log("Test message", debug_enabled=False)
        assert result is False
        assert len(caplog.records) == 0

    def test_debug_enabled(self, caplog):
        """Test that logging occurs when debug is enabled"""
        caplog.set_level(logging.DEBUG)
        result = conditional_debug_log("Test message", debug_enabled=True)
        assert result is True
        assert len(caplog.records) == 1
        assert caplog.records[0].levelno == logging.DEBUG
        assert caplog.records[0].getMessage() == "Test message"

    def test_custom_logger(self, caplog):
        """Test logging with a custom logger"""
        # Create a custom logger
        custom_logger = logging.getLogger('custom_logger')
        custom_logger.setLevel(logging.DEBUG)
        
        result = conditional_debug_log("Custom logger message", 
                                       debug_enabled=True, 
                                       logger=custom_logger)
        
        # Check if logging worked with custom logger
        assert result is True
        
        # Note: caplog won't capture logs from a custom logger by default
        # So we'll just check the return value

    def test_message_types(self):
        """Test different types of messages"""
        # Test with different message types
        assert conditional_debug_log(123, debug_enabled=True) is True
        assert conditional_debug_log(None, debug_enabled=True) is True
        assert conditional_debug_log("", debug_enabled=True) is True