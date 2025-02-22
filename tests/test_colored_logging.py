import pytest
import sys
from io import StringIO
from src.colored_logging import log_with_background, BackgroundColors

def test_log_with_background_default():
    """Test logging with default white background."""
    output = StringIO()
    log_with_background("Test Message", file=output)
    result = output.getvalue().strip()
    assert '\033[47mTest Message\033[0m' in result

def test_log_with_background_colors():
    """Test logging with different background colors."""
    colors = [
        BackgroundColors.RED, 
        BackgroundColors.GREEN, 
        BackgroundColors.YELLOW, 
        BackgroundColors.BLUE, 
        BackgroundColors.MAGENTA, 
        BackgroundColors.CYAN
    ]
    
    for color in colors:
        output = StringIO()
        log_with_background("Test Message", color=color, file=output)
        result = output.getvalue().strip()
        assert f'{color}Test Message\033[0m' in result

def test_log_with_background_invalid_color():
    """Test that an invalid color raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid color"):
        log_with_background("Test", color="INVALID_COLOR")

def test_log_with_background_invalid_message_type():
    """Test that non-string message raises a TypeError."""
    with pytest.raises(TypeError, match="Message must be a string"):
        log_with_background(123)
    with pytest.raises(TypeError, match="Message must be a string"):
        log_with_background(None)