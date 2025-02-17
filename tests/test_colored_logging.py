import io
import pytest
from src.colored_logging import log_with_background, BackgroundColors

def test_log_with_background_default():
    """Test logging with default white background."""
    output = io.StringIO()
    log_with_background("Test Message", file=output)
    result = output.getvalue().strip()
    assert result == f"\033[47mTest Message\033[49m"

def test_log_with_background_specific_color():
    """Test logging with a specific background color."""
    output = io.StringIO()
    log_with_background("Error Message", color=BackgroundColors.RED, file=output)
    result = output.getvalue().strip()
    assert result == f"\033[41mError Message\033[49m"

def test_log_with_background_invalid_type():
    """Test that logging fails for non-string input."""
    with pytest.raises(TypeError, match="Message must be a string"):
        log_with_background(123)

def test_log_with_background_invalid_color():
    """Test that logging fails for invalid color."""
    with pytest.raises(ValueError, match="Invalid color. Use colors from BackgroundColors class"):
        log_with_background("Test", color="invalid_color")

def test_all_background_colors_available():
    """Verify all background colors are accessible and can be used."""
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
        log_with_background("Test", color=color, file=output)
        assert output.getvalue().strip() is not None