import pytest
from src.font_logger import FontLogger

def test_default_logging():
    """Test default logging without specifying size"""
    result = FontLogger.log("Default message")
    assert "Default message" in result

def test_small_font_logging():
    """Test small font logging"""
    result = FontLogger.log("Small message", size='small')
    assert "Small message" in result
    assert result.startswith('\033[92m')
    assert result.endswith('\033[0m')

def test_medium_font_logging():
    """Test medium font logging"""
    result = FontLogger.log("Medium message", size='medium')
    assert "Medium message" in result
    assert result.startswith('\033[93m')
    assert result.endswith('\033[0m')

def test_large_font_logging():
    """Test large font logging"""
    result = FontLogger.log("Large message", size='large')
    assert "Large message" in result
    assert result.startswith('\033[91m')
    assert result.endswith('\033[0m')

def test_invalid_font_size():
    """Test that an invalid font size raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid font size"):
        FontLogger.log("Invalid message", size='extra-large')