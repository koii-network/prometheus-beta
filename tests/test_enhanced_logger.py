import pytest
from src.enhanced_logger import EnhancedLogger

def test_default_logging():
    """Test default logging behavior"""
    result = EnhancedLogger.log("Default message")
    assert "Default message" in result

def test_font_sizes():
    """Test all supported font sizes"""
    sizes = ['small', 'normal', 'large', 'huge']
    for size in sizes:
        result = EnhancedLogger.log(f"Test {size} message", size)
        assert f"Test {size} message" in result

def test_invalid_font_size():
    """Test that an invalid font size raises a ValueError"""
    with pytest.raises(ValueError, match="Unsupported font size"):
        EnhancedLogger.log("Invalid size message", "extra-large")

def test_output_contains_message():
    """Verify that the log method returns the full styled message"""
    message = "Hello, World!"
    result = EnhancedLogger.log(message, 'large')
    assert message in result