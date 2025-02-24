import io
import pytest
from src.colored_logger import BackgroundColorLogger

def test_log_with_background_color():
    """Test logging with a background color"""
    # Capture stdout
    captured_output = io.StringIO()
    
    # Log a message with background color
    BackgroundColorLogger.log("Test message", bg_color='red', file=captured_output)
    
    # Check if the output contains the correct ANSI color code
    output = captured_output.getvalue().strip()
    assert '\033[41mTest message\033[0m' in output

def test_log_invalid_background_color():
    """Test that an invalid background color raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid background color"):
        BackgroundColorLogger.log("Test message", bg_color='invalid_color')

def test_log_multiple_messages():
    """Test logging multiple messages with different background colors"""
    captured_output = io.StringIO()
    
    # Log multiple messages
    BackgroundColorLogger.log("First message", bg_color='green', file=captured_output)
    BackgroundColorLogger.log("Second message", bg_color='blue', file=captured_output)
    
    # Check output
    output = captured_output.getvalue()
    assert '\033[42mFirst message\033[0m' in output
    assert '\033[44mSecond message\033[0m' in output

def test_text_color_not_implemented():
    """Test that text coloring raises NotImplementedError"""
    with pytest.raises(NotImplementedError):
        BackgroundColorLogger.color_text("Test", "red")

def test_log_no_color():
    """Test logging without a background color"""
    captured_output = io.StringIO()
    
    # Log a message without color
    BackgroundColorLogger.log("No color message", file=captured_output)
    
    # Check output
    output = captured_output.getvalue().strip()
    assert output == "No color message"