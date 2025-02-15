import logging
import pytest
from src.logging_utils import log_multiple

class TestLogging:
    def test_default_logging(self, caplog):
        """Test default info level logging"""
        caplog.set_level(logging.INFO)
        log_multiple("Test", 123, "message")
        assert "Test 123 message" in caplog.text
    
    def test_different_log_levels(self, caplog):
        """Test different logging levels"""
        levels = ['debug', 'warning', 'error', 'critical']
        for level in levels:
            caplog.clear()
            caplog.set_level(getattr(logging, level.upper()))
            log_multiple("Test", level, "logging", level=level)
            assert f"Test {level} logging" in caplog.text
    
    def test_mixed_type_logging(self, caplog):
        """Test logging with mixed types"""
        caplog.set_level(logging.INFO)
        log_multiple(42, "is", ["the", "answer"], {"key": "value"})
        assert "42 is ['the', 'answer'] {'key': 'value'}" in caplog.text
    
    def test_invalid_log_level(self):
        """Test that invalid log level raises ValueError"""
        with pytest.raises(ValueError, match="Invalid logging level"):
            log_multiple("Invalid", "level", level="nonexistent")
    
    def test_custom_logger(self, caplog):
        """Test logging with a custom logger"""
        custom_logger = logging.getLogger('custom_logger')
        caplog.set_level(logging.INFO, logger=custom_logger)
        log_multiple("Custom", "logger", "test", logger=custom_logger, level='info')
        assert "Custom logger test" in caplog.text