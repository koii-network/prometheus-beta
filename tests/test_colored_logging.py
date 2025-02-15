import pytest
from src.colored_logging import ColoredLogger

def test_log_without_color(capsys):
    """Test logging a message without color."""
    ColoredLogger.log("Test message")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Test message"

def test_log_with_valid_background_color(capsys):
    """Test logging a message with a valid background color."""
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    for color in colors:
        ColoredLogger.log("Colored message", background_color=color)
        captured = capsys.readouterr()
        assert f"\033[4{colors.index(color)+1}m" in captured.out
        assert "Colored message" in captured.out
        assert "\033[0m" in captured.out

def test_log_with_invalid_background_color():
    """Test that an invalid background color raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid background color"):
        ColoredLogger.log("Test message", background_color="invalid_color")

def test_log_case_insensitive_color(capsys):
    """Test that background color is case-insensitive."""
    ColoredLogger.log("Mixed case color", background_color="ReD")
    captured = capsys.readouterr()
    assert "\033[41m" in captured.out