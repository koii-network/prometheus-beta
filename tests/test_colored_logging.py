import io
import pytest
from src.colored_logging import log_with_background, BackgroundColors

def test_log_with_background_default():
    """Test logging with default background color."""
    output = io.StringIO()
    log_with_background("Test message", file=output)
    result = output.getvalue().strip()
    assert result.startswith('\033[47m')
    assert result.endswith('\033[0m')
    assert "Test message" in result

def test_log_with_background_specific_colors():
    """Test logging with different background colors."""
    colors = [
        BackgroundColors.RED, 
        BackgroundColors.GREEN, 
        BackgroundColors.YELLOW,
        BackgroundColors.BLUE, 
        BackgroundColors.MAGENTA, 
        BackgroundColors.CYAN, 
        BackgroundColors.WHITE
    ]
    
    for color in colors:
        output = io.StringIO()
        log_with_background("Test message", color=color, file=output)
        result = output.getvalue().strip()
        assert result.startswith(color)
        assert result.endswith('\033[0m')
        assert "Test message" in result

def test_log_with_background_invalid_color():
    """Test that an invalid color raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid background color"):
        log_with_background("Test message", color="invalid_color")

def test_log_with_background_invalid_message_type():
    """Test that non-string message raises a TypeError."""
    with pytest.raises(TypeError, match="Message must be a string"):
        log_with_background(123)  # Integer instead of string

def test_log_with_background_empty_string():
    """Test logging an empty string."""
    output = io.StringIO()
    log_with_background("", file=output)
    result = output.getvalue().strip()
    assert result.startswith('\033[47m')
    assert result.endswith('\033[0m')
    assert result == '\033[47m\033[0m'