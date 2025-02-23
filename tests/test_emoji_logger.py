import logging
import pytest
from src.emoji_logger import log_with_emoji

def test_default_logging(caplog):
    """Test default logging with default emoji and level."""
    caplog.set_level(logging.INFO)
    log_with_emoji("Test message")
    assert "ð Test message" in caplog.text

def test_different_emoji(caplog):
    """Test logging with a different emoji."""
    caplog.set_level(logging.INFO)
    log_with_emoji("Warning message", emoji='â ï¸')
    assert "â ï¸ Warning message" in caplog.text

def test_different_log_levels(caplog):
    """Test logging with different log levels."""
    log_levels = [
        ('debug', logging.DEBUG),
        ('info', logging.INFO),
        ('warning', logging.WARNING),
        ('error', logging.ERROR),
        ('critical', logging.CRITICAL)
    ]
    
    for level_name, log_level in log_levels:
        caplog.clear()
        caplog.set_level(log_level)
        log_with_emoji(f"Test {level_name} message", level=level_name)
        assert f"ð Test {level_name} message" in caplog.text

def test_invalid_log_level():
    """Test that an invalid log level raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid log level"):
        log_with_emoji("Test message", level="invalid")