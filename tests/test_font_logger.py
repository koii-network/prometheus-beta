import pytest
from src.font_logger import FontLogger

def test_default_font_size():
    """Test the default font size (3)"""
    result = FontLogger.log("Hello World")
    assert "[medium font] Hello World" in result

def test_different_font_sizes():
    """Test different valid font sizes"""
    sizes_to_test = [1, 2, 3, 4, 5, 6]
    expected_sizes = [
        "small", 
        "medium-small", 
        "medium", 
        "medium-large", 
        "large", 
        "extra-large"
    ]
    
    for size, expected_size in zip(sizes_to_test, expected_sizes):
        result = FontLogger.log(f"Test message for size {size}", size)
        assert f"[{expected_size} font]" in result

def test_invalid_font_size_low():
    """Test invalid font size (too low)"""
    with pytest.raises(ValueError, match="Font size must be an integer between 1 and 6"):
        FontLogger.log("Test message", 0)

def test_invalid_font_size_high():
    """Test invalid font size (too high)"""
    with pytest.raises(ValueError, match="Font size must be an integer between 1 and 6"):
        FontLogger.log("Test message", 7)

def test_invalid_font_size_type():
    """Test invalid font size type"""
    with pytest.raises(ValueError, match="Font size must be an integer between 1 and 6"):
        FontLogger.log("Test message", "large")