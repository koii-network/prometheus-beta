import pytest
import logging
import sys
from io import StringIO
from src.custom_logger import log_with_style

def test_log_with_style_default():
    # Capture logging output
    captured_output = StringIO()
    logging.basicConfig(stream=captured_output, level=logging.INFO)
    
    log_with_style("Test message")
    
    output = captured_output.getvalue()
    assert "Test message" in output

def test_log_with_style_different_levels():
    levels = ['debug', 'info', 'warning', 'error', 'critical']
    
    for level in levels:
        # Capture logging output
        captured_output = StringIO()
        logging.basicConfig(stream=captured_output, level=logging.DEBUG)
        
        log_with_style(f"Test {level.upper()} message", level=level)
        
        output = captured_output.getvalue()
        assert f"Test {level.upper()} message" in output

def test_log_with_style_invalid_level():
    with pytest.raises(ValueError, match="Invalid logging level"):
        log_with_style("Test message", level="invalid")

def test_log_with_style_color_and_styles():
    # This test verifies that color and style parameters work without raising errors
    captured_output = StringIO()
    logging.basicConfig(stream=captured_output, level=logging.INFO)
    
    log_with_style("Colored bold message", color='green', bold=True)
    log_with_style("Underlined message", underline=True)
    
    output = captured_output.getvalue()
    assert "Colored bold message" in output
    assert "Underlined message" in output