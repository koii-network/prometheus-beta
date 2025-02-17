import io
import sys
from src.logger import log_message

def test_log_message(capsys):
    """
    Test that log_message prints the correct message to the console.
    """
    test_msg = "Hello, logging test!"
    log_message(test_msg)
    
    # Capture the printed output
    captured = capsys.readouterr()
    
    # Assert that the printed message matches the input
    assert captured.out.strip() == test_msg

def test_log_message_empty_string(capsys):
    """
    Test logging an empty string.
    """
    log_message("")
    captured = capsys.readouterr()
    assert captured.out.strip() == ""

def test_log_message_non_string_input(capsys):
    """
    Test logging a non-string input (should be converted to string).
    """
    test_obj = {"key": "value"}
    log_message(test_obj)
    captured = capsys.readouterr()
    assert captured.out.strip() == str(test_obj)