import sys
from io import StringIO
import pytest
from src.bold_logger import log_bold

def test_log_bold_output():
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    # Call the function
    log_bold("Test Message")

    # Reset redirect
    sys.stdout = sys.__stdout__

    # Check the output
    output = captured_output.getvalue().strip()
    
    # The output should contain ANSI bold codes and the message
    assert "\033[1mTest Message\033[0m" in output

def test_log_bold_different_messages():
    test_messages = [
        "Hello World",
        "Python Logging",
        "123456",
        ""  # Empty string
    ]

    for message in test_messages:
        captured_output = StringIO()
        sys.stdout = captured_output

        log_bold(message)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        
        assert "\033[1m" + message + "\033[0m" in output