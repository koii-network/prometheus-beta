import pytest
import sys
from io import StringIO
from src.color_logger import log_colored_message
from colorama import Fore, Style

def test_default_white_color():
    # Redirect stdout to capture print output
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Log a message
    log_colored_message("Test message")
    
    # Reset redirect
    sys.stdout = sys.__stdout__
    
    # Check output contains white color code and message
    assert f"{Fore.WHITE}Test message{Style.RESET_ALL}" in captured_output.getvalue()

def test_specific_colors():
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
    color_codes = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN
    }
    
    for color in colors:
        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Log a message with specific color
        log_colored_message("Test message", color)
        
        # Reset redirect
        sys.stdout = sys.__stdout__
        
        # Check output contains correct color code and message
        assert f"{color_codes[color]}Test message{Style.RESET_ALL}" in captured_output.getvalue()

def test_invalid_color():
    with pytest.raises(ValueError, match="Unsupported color"):
        log_colored_message("Test message", "purple")