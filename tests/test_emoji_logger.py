import pytest
import logging
import io
import sys
from src.emoji_logger import log_with_emoji

def test_default_log_with_emoji(caplog):
    """Test default logging with emoji"""
    caplog.set_level(logging.INFO)
    log_with_emoji("Test message")
    assert "✨ Test message" in caplog.text
    assert len(caplog.records) == 1

def test_different_emoji_log(caplog):
    """Test logging with a different emoji"""
    caplog.set_level(logging.WARNING)
    log_with_emoji("Warning message", level='warning', emoji='⚠️')
    assert "⚠️ Warning message" in caplog.text

def test_log_levels(caplog):
    """Test different log levels"""
    log_levels = ['debug', 'info', 'warning', 'error', 'critical']
    for level in log_levels:
        caplog.clear()
        caplog.set_level(logging.DEBUG)
        log_with_emoji(f"{level.upper()} test", level=level)
        assert len(caplog.records) == 1
        assert caplog.records[0].levelname.lower() == level

def test_invalid_log_level():
    """Test raising ValueError for invalid log level"""
    with pytest.raises(ValueError, match="Invalid log level"):
        log_with_emoji("Test", level='invalid_level')