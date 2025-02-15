import io
import sys
import pytest
from src.indented_logger import log_with_indent

def test_default_logging():
    """Test default logging without indentation"""
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    log_with_indent("Test message")
    sys.stdout = sys.__stdout__
    
    assert captured_output.getvalue().strip() == "Test message"

def test_indentation():
    """Test logging with different indentation levels"""
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    log_with_indent("Level 0 message")
    log_with_indent("Level 1 message", indent_level=1)
    log_with_indent("Level 2 message", indent_level=2)
    
    sys.stdout = sys.__stdout__
    
    expected_output = """Level 0 message
    Level 1 message
        Level 2 message"""
    
    assert captured_output.getvalue().strip() == expected_output.strip()

def test_custom_file_output():
    """Test logging to a custom file-like object"""
    custom_output = io.StringIO()
    log_with_indent("Custom output message", file=custom_output)
    
    assert custom_output.getvalue().strip() == "Custom output message"

def test_input_validation():
    """Test handling of different input types"""
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Test with different types of messages
    log_with_indent(42)  # Integer
    log_with_indent(True)  # Boolean
    log_with_indent(3.14)  # Float
    
    sys.stdout = sys.__stdout__
    
    expected_output = """42
True
3.14"""
    
    assert captured_output.getvalue().strip() == expected_output.strip()