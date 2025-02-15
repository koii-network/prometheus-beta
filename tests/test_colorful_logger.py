import pytest
from termcolor import colored
from src.colorful_logger import log_colored

def test_default_green_color(capsys):
    """Test that default color is green"""
    log_colored("Test message")
    captured = capsys.readouterr()
    assert colored("Test message", 'green') in captured.out

def test_different_colors(capsys):
    """Test logging with different supported colors"""
    colors = ['red', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    for color in colors:
        log_colored("Test message", color)
        captured = capsys.readouterr()
        assert colored("Test message", color) in captured.out

def test_unsupported_color():
    """Test that an unsupported color raises a ValueError"""
    with pytest.raises(ValueError, match="Unsupported color"):
        log_colored("Test message", "orange")

def test_return_value():
    """Test that the function returns the colored message"""
    result = log_colored("Test message", "blue")
    assert result == colored("Test message", "blue")