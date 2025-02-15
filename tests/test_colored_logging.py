import pytest
from src.colored_logging import log_colored_message
from colorama import Fore, Style

def test_default_green_color():
    """Test default color is green"""
    message = "Test message"
    expected = f"{Fore.GREEN}{message}{Style.RESET_ALL}"
    assert log_colored_message(message) == expected

def test_different_colors():
    """Test different color outputs"""
    colors = ['RED', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN']
    color_map = {
        'RED': Fore.RED,
        'YELLOW': Fore.YELLOW,
        'BLUE': Fore.BLUE,
        'MAGENTA': Fore.MAGENTA,
        'CYAN': Fore.CYAN
    }
    
    for color in colors:
        message = f"Test {color} message"
        expected = f"{color_map[color]}{message}{Style.RESET_ALL}"
        assert log_colored_message(message, color) == expected

def test_case_insensitive_color():
    """Test that color is case-insensitive"""
    message = "Mixed case color"
    expected = f"{Fore.GREEN}{message}{Style.RESET_ALL}"
    assert log_colored_message(message, 'gReEn') == expected

def test_invalid_color():
    """Test that an invalid color raises a ValueError"""
    with pytest.raises(ValueError, match="Unsupported color: ORANGE"):
        log_colored_message("Test message", "ORANGE")

def test_empty_message():
    """Test logging an empty message"""
    message = ""
    expected = f"{Fore.GREEN}{message}{Style.RESET_ALL}"
    assert log_colored_message(message) == expected