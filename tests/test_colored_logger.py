import io
import pytest
import sys

from src.colored_logger import log_with_background, BackgroundColors

def test_log_without_background():
    """Test logging without a background color."""
    # Capture stdout
    captured_output = io.StringIO()
    log_with_background("Test message", file=captured_output)
    assert captured_output.getvalue().strip() == "Test message"

def test_log_with_background_colors():
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
        captured_output = io.StringIO()
        log_with_background("Colored message", background_color=color, file=captured_output)
        output = captured_output.getvalue().strip()
        assert output.startswith(color)
        assert output.endswith(BackgroundColors.RESET)
        assert "Colored message" in output

def test_invalid_background_color():
    """Test that an invalid background color raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid background color"):
        log_with_background("Test", background_color="invalid_color")

def test_invalid_message_type():
    """Test that non-string message raises a TypeError."""
    with pytest.raises(TypeError, match="Message must be a string"):
        log_with_background(123)
    with pytest.raises(TypeError, match="Message must be a string"):
        log_with_background(None)

def test_empty_message():
    """Test logging an empty string."""
    captured_output = io.StringIO()
    log_with_background("", file=captured_output)
    assert captured_output.getvalue().strip() == ""

def test_message_with_special_characters():
    """Test logging a message with special characters and colors."""
    captured_output = io.StringIO()
    log_with_background("Hello, World! @#$%^&*()", 
                        background_color=BackgroundColors.GREEN, 
                        file=captured_output)
    output = captured_output.getvalue().strip()
    assert output.startswith(BackgroundColors.GREEN)
    assert output.endswith(BackgroundColors.RESET)
    assert "Hello, World! @#$%^&*()" in output