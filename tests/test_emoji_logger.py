import pytest
import logging
from src.emoji_logger import log_with_emoji

def test_default_info_logging(caplog):
    """Test default info logging with default emoji"""
    caplog.set_level(logging.INFO)
    result = log_with_emoji("Test message")
    assert "ℹ️ Test message" in result
    assert len(caplog.records) == 1

def test_custom_emoji_logging():
    """Test logging with a custom emoji"""
    result = log_with_emoji("Custom message", emoji_symbol="🌟")
    assert "🌟 Custom message" in result

def test_different_log_levels(caplog):
    """Test all different log levels"""
    log_levels = [
        ('debug', '🔍'),
        ('info', 'ℹ️'),
        ('warning', '⚠️'),
        ('error', '❌'),
        ('critical', '🚨')
    ]
    
    for level, expected_emoji in log_levels:
        caplog.clear()
        caplog.set_level(logging.DEBUG)
        result = log_with_emoji(f"Test {level} message", level=level)
        assert f"{expected_emoji} Test {level} message" in result

def test_invalid_log_level():
    """Test that an invalid log level raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid log level"):
        log_with_emoji("Invalid message", level="invalid")

def test_emoji_symbol_replacement():
    """Test that custom emoji can replace default emoji"""
    result = log_with_emoji("Replacement test", level="error", emoji_symbol="🚀")
    assert "🚀 Replacement test" in result