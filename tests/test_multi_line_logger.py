import logging
import io
import sys
import pytest
from src.multi_line_logger import log_multiline

def test_log_multiline_default():
    """Test default logging behavior"""
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Configure logging to write to stdout
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, 
                        format='%(message)s')

    message = "Test multi-line logging"
    sep_line = log_multiline(message)

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Get the captured output and split into lines
    output_lines = captured_output.getvalue().strip().split('\n')

    assert len(output_lines) == 3
    assert output_lines[0] == '*' * 40
    assert output_lines[1] == message
    assert output_lines[2] == '*' * 40
    assert sep_line == '*' * 40

def test_log_multiline_custom_params():
    """Test logging with custom separator and length"""
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Configure logging to write to stdout
    logging.basicConfig(stream=sys.stdout, level=logging.WARNING, 
                        format='%(message)s')

    message = "Custom logging test"
    sep_line = log_multiline(message, 
                              level=logging.WARNING, 
                              separator='-', 
                              separator_length=20)

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Get the captured output and split into lines
    output_lines = captured_output.getvalue().strip().split('\n')

    assert len(output_lines) == 3
    assert output_lines[0] == '-' * 20
    assert output_lines[1] == message
    assert output_lines[2] == '-' * 20
    assert sep_line == '-' * 20

def test_log_multiline_error_cases():
    """Test error handling for invalid inputs"""
    # Non-string message
    with pytest.raises(TypeError, match="Message must be a string"):
        log_multiline(123)
    
    # Non-string separator
    with pytest.raises(TypeError, match="Separator must be a string"):
        log_multiline("Test", separator=123)
    
    # Empty separator
    with pytest.raises(ValueError, match="Separator cannot be an empty string"):
        log_multiline("Test", separator='')
    
    # Invalid separator length
    with pytest.raises(ValueError, match="Separator length must be at least 1"):
        log_multiline("Test", separator_length=0)