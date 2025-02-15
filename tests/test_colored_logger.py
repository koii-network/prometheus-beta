import sys
import io
import pytest
from src.colored_logger import ColoredLogger

def test_default_logging():
    """Test default white background logging"""
    output = io.StringIO()
    ColoredLogger.log("Test Message", file=output)
    result = output.getvalue().strip()
    assert '\033[47m\033[37mTest Message\033[0m' in result

def test_custom_background_color():
    """Test logging with custom background color"""
    output = io.StringIO()
    ColoredLogger.log("Blue Background", bg_color='blue', file=output)
    result = output.getvalue().strip()
    assert '\033[44m\033[37mBlue Background\033[0m' in result

def test_custom_text_color():
    """Test logging with custom text color"""
    output = io.StringIO()
    ColoredLogger.log("Yellow Background", bg_color='yellow', text_color='black', file=output)
    result = output.getvalue().strip()
    assert '\033[43m\033[30mYellow Background\033[0m' in result

def test_invalid_background_color():
    """Test that an invalid background color raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid background color"):
        ColoredLogger.log("Invalid Color", bg_color='purple')

def test_all_background_colors():
    """Verify all supported background colors can be used"""
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    for color in colors:
        output = io.StringIO()
        ColoredLogger.log(f"{color.capitalize()} Background", bg_color=color, file=output)
        result = output.getvalue().strip()
        assert f'\033[4{colors.index(color)+1}m' in result