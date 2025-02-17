import pytest
import sys
from io import StringIO
from src.colored_logging import log_colored_message
from colorama import Fore, Style

def test_default_green_logging():
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Log a message
    log_colored_message("Test message")
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check output
    assert f"{Fore.GREEN}Test message{Style.RESET_ALL}" in captured_output.getvalue()

def test_specific_color_logging():
    colors = ['RED', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN']
    
    for color in colors:
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Log a message
        log_colored_message(f"Test {color} message", color)
        
        # Restore stdout
        sys.stdout = sys.__stdout__
        
        # Check output
        expected_color = getattr(Fore, color)
        assert f"{expected_color}Test {color} message{Style.RESET_ALL}" in captured_output.getvalue()

def test_invalid_color_raises_error():
    with pytest.raises(ValueError, match="Unsupported color"):
        log_colored_message("Test message", "PURPLE")